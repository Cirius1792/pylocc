import subprocess
import time
import os
import click
from pathlib import Path
import shutil

# Define sample repositories to benchmark
SAMPLE_REPOS = {
    "valkey": "https://github.com/valkey-io/valkey",
    "linux": "https://github.com/torvalds/linux",
    "java-spelling-corrector": "https://github.com/boyter/java-spelling-corrector",
}

@click.command()
@click.argument('target_path', type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True), required=False)
@click.option('--temp-dir', default='./benchmark_repos', help='Directory to clone repositories into (if no target_path is specified).')
@click.option('--clean', is_flag=True, help='Clean up cloned repositories after benchmarking (if no target_path is specified).')
def benchmark(target_path, temp_dir, clean):
    """
    Benchmarks pylocc against scc for counting lines of code.
    Can benchmark a specific TARGET_PATH or predefined sample repositories.
    """

    def run_single_benchmark(path_to_benchmark):
        click.echo(f"\nBenchmarking: {Path(path_to_benchmark).name}")

        # --- Benchmark pylocc ---
        pylocc_command = ["uv", "run", "pylocc", str(path_to_benchmark)]
        click.echo(f"  Running pylocc: {' '.join(pylocc_command)}")
        start_time = time.time()
        try:
            pylocc_result = subprocess.run(pylocc_command, capture_output=True, text=True, check=True)
            pylocc_time = time.time() - start_time
            click.echo(f"  pylocc completed in: {pylocc_time:.4f} seconds")
            # Optional: print pylocc_result.stdout if you want to see the output
        except subprocess.CalledProcessError as e:
            click.echo(f"  Error running pylocc: {e}", err=True)
            click.echo(f"  Stdout: {e.stdout}", err=True)
            click.echo(f"  Stderr: {e.stderr}", err=True)
            pylocc_time = float('inf') # Mark as failed

        # --- Benchmark scc ---
        scc_command = ["scc", str(path_to_benchmark)]
        click.echo(f"  Running scc: {' '.join(scc_command)}")
        start_time = time.time()
        try:
            scc_result = subprocess.run(scc_command, capture_output=True, text=True, check=True)
            scc_time = time.time() - start_time
            click.echo(f"  scc completed in: {scc_time:.4f} seconds")
            # Optional: print scc_result.stdout if you want to see the output
        except FileNotFoundError:
            click.echo("  scc command not found. Please install scc to benchmark against it.", err=True)
            click.echo("  You can usually install it from your package manager (e.g., `sudo apt install scc`) or download from https://github.com/boyter/scc/releases", err=True)
            scc_time = float('inf') # Mark as failed
        except subprocess.CalledProcessError as e:
            click.echo(f"  Error running scc: {e}", err=True)
            click.echo(f"  Stdout: {e.stdout}", err=True)
            click.echo(f"  Stderr: {e.stderr}", err=True)
            scc_time = float('inf') # Mark as failed

        # --- Compare Results ---
        click.echo("  --- Summary ---")
        click.echo(f"  pylocc: {pylocc_time:.4f} seconds")
        click.echo(f"  scc:    {scc_time:.4f} seconds")

        if pylocc_time < scc_time:
            if scc_time != float('inf'):
                click.echo(f"  pylocc was {scc_time / pylocc_time:.2f}x faster than scc.")
            else:
                click.echo("  pylocc succeeded while scc failed.")
        elif scc_time < pylocc_time:
            if pylocc_time != float('inf'):
                click.echo(f"  scc was {pylocc_time / scc_time:.2f}x faster than pylocc.")
            else:
                click.echo("  scc succeeded while pylocc failed.")
        else:
            click.echo("  pylocc and scc took approximately the same amount of time (or both failed).")

    if target_path:
        # Benchmark a specific path
        click.echo(f"Benchmarking specified path: {target_path}")
        run_single_benchmark(target_path)
    else:
        # Benchmark sample repositories
        temp_path = Path(temp_dir).resolve()
        temp_path.mkdir(parents=True, exist_ok=True)

        click.echo(f"Cloning repositories into: {temp_path}")

        cloned_paths = []
        for repo_name, repo_url in SAMPLE_REPOS.items():
            repo_path = temp_path / repo_name
            if not repo_path.exists():
                click.echo(f"Cloning {repo_name}...")
                try:
                    subprocess.run(["git", "clone", repo_url, str(repo_path)], check=True, capture_output=True)
                    cloned_paths.append(repo_path)
                except subprocess.CalledProcessError as e:
                    click.echo(f"Error cloning {repo_name}: {e.stderr.decode()}", err=True)
                    continue
            else:
                click.echo(f"Repository {repo_name} already exists at {repo_path}. Skipping clone.")
                cloned_paths.append(repo_path)

        if not cloned_paths:
            click.echo("No repositories available for benchmarking. Exiting.", err=True)
            return

        click.echo("\n--- Starting Benchmarks ---")

        for path_to_benchmark in cloned_paths:
            run_single_benchmark(path_to_benchmark)

        if clean:
            click.echo(f"\nCleaning up {temp_path}...")
            shutil.rmtree(temp_path)
            click.echo("Cleanup complete.")

if __name__ == '__main__':
    benchmark()