import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <img src="/pylocc/img/pylocc_logo_transparent.png" alt="pylocc logo" width="350" />
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Get Started
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <div className={styles.section}>
          <div className="container">
            <div className="row">
              <div className={clsx('col col--12')}>
                <Heading as="h2">Install with pip</Heading>
                <p>
                  You can install pylocc using pip. Make sure you have Python 3.10 or higher installed.
                </p>
                <pre><code>pip install pylocc</code></pre>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
