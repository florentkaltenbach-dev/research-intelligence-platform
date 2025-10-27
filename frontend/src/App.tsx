import { Routes, Route, Link } from 'react-router-dom'
import HomePage from './pages/HomePage'
import EventsPage from './pages/EventsPage'
import EventDetailPage from './pages/EventDetailPage'
import EventTimelinePage from './pages/EventTimelinePage'
import MetricsPage from './pages/MetricsPage'
import MetricDetailPage from './pages/MetricDetailPage'
import SourcesPage from './pages/SourcesPage'
import AnalysesPage from './pages/AnalysesPage'
import AnalysisDetailPage from './pages/AnalysisDetailPage'
import HistoricalPatternsPage from './pages/HistoricalPatternsPage'
import AboutPage from './pages/AboutPage'

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              <Link to="/" className="flex items-center">
                <span className="text-xl font-bold text-gray-900">
                  Research Intelligence Platform
                </span>
              </Link>
              <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                <Link
                  to="/events"
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600"
                >
                  Events
                </Link>
                <Link
                  to="/timeline"
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600"
                >
                  Timeline
                </Link>
                <Link
                  to="/metrics"
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600"
                >
                  Metrics
                </Link>
                <Link
                  to="/sources"
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600"
                >
                  Sources
                </Link>
                <Link
                  to="/analyses"
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600"
                >
                  Analyses
                </Link>
                <Link
                  to="/historical-patterns"
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600"
                >
                  Patterns
                </Link>
                <Link
                  to="/about"
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 hover:text-blue-600"
                >
                  About
                </Link>
              </div>
            </div>
          </div>
        </nav>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/events" element={<EventsPage />} />
          <Route path="/events/:id" element={<EventDetailPage />} />
          <Route path="/timeline" element={<EventTimelinePage />} />
          <Route path="/metrics" element={<MetricsPage />} />
          <Route path="/metrics/:id" element={<MetricDetailPage />} />
          <Route path="/sources" element={<SourcesPage />} />
          <Route path="/analyses" element={<AnalysesPage />} />
          <Route path="/analyses/:id" element={<AnalysisDetailPage />} />
          <Route path="/historical-patterns" element={<HistoricalPatternsPage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <p className="text-center text-sm text-gray-500">
            Research Intelligence Platform - Analyzing global power transitions
          </p>
        </div>
      </footer>
    </div>
  )
}

export default App
