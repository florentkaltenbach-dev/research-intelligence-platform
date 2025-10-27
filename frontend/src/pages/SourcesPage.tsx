import { useQuery } from '@tanstack/react-query'
import { getSources } from '../services/api'
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip, BarChart, Bar, XAxis, YAxis, CartesianGrid } from 'recharts'

const TIER_COLORS = {
  tier_1: 'bg-green-100 text-green-800',
  tier_2: 'bg-blue-100 text-blue-800',
  tier_3: 'bg-yellow-100 text-yellow-800',
  tier_4: 'bg-gray-100 text-gray-800',
}

const CHART_COLORS = ['#10b981', '#3b82f6', '#eab308', '#6b7280']

export default function SourcesPage() {
  const { data: sources, isLoading } = useQuery({
    queryKey: ['sources'],
    queryFn: async () => {
      const response = await getSources()
      return response.data
    },
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading sources...</div>
  }

  // Calculate diversity metrics
  const tierCounts: { [key: string]: number } = {}
  const languageCounts: { [key: string]: number } = {}
  const regionCounts: { [key: string]: number } = {}

  sources?.forEach((source: any) => {
    // Count by tier
    const tier = source.credibility_tier || 'unknown'
    tierCounts[tier] = (tierCounts[tier] || 0) + 1

    // Count by language
    const lang = source.language || 'Unknown'
    languageCounts[lang] = (languageCounts[lang] || 0) + 1

    // Count by region
    const region = source.region || 'Unknown'
    regionCounts[region] = (regionCounts[region] || 0) + 1
  })

  const tierData = Object.entries(tierCounts).map(([tier, count]) => ({
    name: tier.replace('_', ' ').toUpperCase(),
    value: count,
  }))

  const languageData = Object.entries(languageCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([language, count]) => ({
      name: language,
      value: count,
    }))

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Source Library</h1>
        <p className="text-gray-600">Sources are rated from Tier 1 (most credible) to Tier 4</p>
      </div>

      {sources && sources.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Credibility Tier Distribution */}
          <div className="bg-white shadow rounded-lg p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Credibility Tier Distribution</h2>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={tierData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, percent }) => `${name} (${(percent * 100).toFixed(0)}%)`}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {tierData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={CHART_COLORS[index % CHART_COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend />
              </PieChart>
            </ResponsiveContainer>
            <div className="mt-4 text-sm text-gray-600">
              <p>Total sources: {sources.length}</p>
            </div>
          </div>

          {/* Language Diversity */}
          <div className="bg-white shadow rounded-lg p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Language Diversity</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={languageData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#3b82f6" />
              </BarChart>
            </ResponsiveContainer>
            <div className="mt-4 text-sm text-gray-600">
              <p>Unique languages: {Object.keys(languageCounts).length}</p>
            </div>
          </div>
        </div>
      )}

      <div className="bg-white shadow rounded-lg divide-y divide-gray-200">
        {sources && sources.length > 0 ? (
          sources.map((source) => (
            <div key={source.id} className="p-5">
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <a
                    href={source.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-lg font-semibold text-blue-600 hover:text-blue-800"
                  >
                    {source.title}
                  </a>
                  {source.publisher && (
                    <p className="text-sm text-gray-600 mt-1">{source.publisher}</p>
                  )}
                  <div className="flex items-center space-x-3 mt-2 text-sm text-gray-500">
                    {source.region && <span>📍 {source.region}</span>}
                    {source.language && <span>🗣️ {source.language}</span>}
                  </div>
                </div>
                <span
                  className={`ml-4 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                    TIER_COLORS[source.credibility_tier as keyof typeof TIER_COLORS]
                  }`}
                >
                  {source.credibility_tier.replace('_', ' ').toUpperCase()}
                </span>
              </div>
            </div>
          ))
        ) : (
          <div className="p-12 text-center text-gray-500">
            <p className="text-lg mb-2">No sources yet</p>
            <p className="text-sm">Sources will be added as you conduct research with Claude Code</p>
          </div>
        )}
      </div>
    </div>
  )
}
