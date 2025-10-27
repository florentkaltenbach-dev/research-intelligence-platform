export default function AboutPage() {
  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="bg-white shadow rounded-lg p-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-6">About This Platform</h1>

        <div className="prose prose-lg max-w-none">
          <h2>Mission</h2>
          <p>
            The Research Intelligence Platform analyzes global power transitions and capital flows
            through multi-perspective research. We aim to provide comprehensive, balanced analysis
            that goes beyond Western-centric viewpoints.
          </p>

          <h2>Research Methodology</h2>
          <p>Our research follows these principles:</p>
          <ul>
            <li>
              <strong>Multi-perspective</strong>: We actively search for non-Western sources
              (Chinese, Russian, Arabic, Hindi, Middle Eastern perspectives)
            </li>
            <li>
              <strong>Currency diversity</strong>: We track data in Yuan, Rupee, Ruble, Dirham, not
              just Dollar/Euro
            </li>
            <li>
              <strong>Historical context</strong>: We map current events to historical power
              transition patterns
            </li>
            <li>
              <strong>Source credibility</strong>: All sources are rated on a 4-tier system
            </li>
            <li>
              <strong>Explicit uncertainty</strong>: We use confidence levels for all claims
            </li>
          </ul>

          <h2>Research Approaches</h2>
          <p>We use several structured research methodologies:</p>
          <ul>
            <li>
              <strong>Source Diversification</strong>: Finding perspectives from diverse regional
              sources
            </li>
            <li>
              <strong>Historical Matcher</strong>: Mapping current events to historical patterns
            </li>
            <li>
              <strong>Counter Narrative</strong>: Finding and analyzing opposing viewpoints
            </li>
            <li>
              <strong>Data Collection</strong>: Tracking financial metrics over time
            </li>
            <li>
              <strong>Credibility Scorer</strong>: Rating sources and assigning confidence levels
            </li>
            <li>
              <strong>Synthesis</strong>: Combining multiple analyses into cohesive findings
            </li>
          </ul>

          <h2>How This Platform Works</h2>
          <p>
            This is a manually curated research platform. Content is added through research
            sessions using Claude Code, ensuring quality and thoughtful analysis rather than
            automated data aggregation.
          </p>

          <h2>Source Credibility Tiers</h2>
          <ul>
            <li>
              <strong>Tier 1</strong>: Government data, peer-reviewed academic papers
            </li>
            <li>
              <strong>Tier 2</strong>: Established news organizations, official reports
            </li>
            <li>
              <strong>Tier 3</strong>: Independent journalists, credible blogs
            </li>
            <li>
              <strong>Tier 4</strong>: Social media, unverified sources
            </li>
          </ul>

          <h2>Open Source</h2>
          <p>
            This platform is built with modern web technologies and is designed to be transparent
            and extensible. All research is version-controlled and traceable.
          </p>
        </div>
      </div>
    </div>
  )
}
