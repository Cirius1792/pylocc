import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.run import _load_config, _validate_scenario


def test_load_config_from_yaml(tmp_path):
    import yaml
    cfg_file = tmp_path / "test_scenarios.yaml"
    data = {
        "runs": 3,
        "scenarios": [{"name": "A", "repo_url": "https://example.com/a.git"}]
    }
    with open(cfg_file, "w") as f:
        yaml.dump(data, f)

    config = _load_config(Path(str(cfg_file)))
    assert config.runs == 3
    assert len(config.scenarios) == 1
    assert config.scenarios[0]["name"] == "A"


def test_load_config_runs_too_low(tmp_path):
    import yaml
    cfg_file = tmp_path / "bad.yaml"
    data = {"runs": 1, "scenarios": []}
    with open(cfg_file, "w") as f:
        yaml.dump(data, f)

    with pytest.raises(SystemExit):
        _load_config(Path(str(cfg_file)))


def test_load_config_missing_scenarios_key(tmp_path):
    import yaml
    cfg_file = tmp_path / "bad.yaml"
    data = {"runs": 3}
    with open(cfg_file, "w") as f:
        yaml.dump(data, f)

    with pytest.raises(SystemExit):
        _load_config(Path(str(cfg_file)))


def test_validate_scenario_missing_name():
    with pytest.raises(SystemExit):
        _validate_scenario({"repo_url": "https://example.com"})


def test_validate_scenario_missing_repo_url():
    with pytest.raises(SystemExit):
        _validate_scenario({"name": "test"})


def test_validate_scenario_valid_passes():
    assert _validate_scenario({"name": "ok", "repo_url": "https://x.git"}) is None
