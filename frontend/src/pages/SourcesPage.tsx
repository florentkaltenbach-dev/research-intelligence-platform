import { useQuery } from '@tanstack/react-query'
import { getSources } from '../services/api'

const TIER_COLORS = {
  tier_1: 'bg-green-100 text-green-800',
  tier_2: 'bg-blue-100 text-blue-800',
  tier_3: 'bg-yellow-100 text-yellow-800',
  tier_4: 'bg-gray-100 text-gray-800',
}

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

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Source Library</h1>
        <p className="text-gray-600">Sources are rated from Tier 1 (most credible) to Tier 4</p>
      </div>

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
