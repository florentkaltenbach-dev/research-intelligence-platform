import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getHistoricalPatterns } from '../services/api'

export default function HistoricalPatternsPage() {
  const { data: patterns, isLoading } = useQuery({
    queryKey: ['historical-patterns'],
    queryFn: async () => {
      const response = await getHistoricalPatterns()
      return response.data
    },
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading historical patterns...</div>
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Historical Patterns</h1>
        <p className="mt-2 text-gray-600">
          Historical power transition patterns that provide context for current events
        </p>
      </div>

      <div className="space-y-4">
        {patterns && patterns.length > 0 ? (
          patterns.map((pattern) => (
            <div key={pattern.id} className="bg-white shadow rounded-lg p-6">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3">
                    <h2 className="text-xl font-semibold text-gray-900">
                      {pattern.name}
                    </h2>
                    {pattern.time_period && (
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                        {pattern.time_period}
                      </span>
                    )}
                  </div>

                  <p className="mt-3 text-gray-700">{pattern.description}</p>

                  {pattern.key_characteristics && pattern.key_characteristics.length > 0 && (
                    <div className="mt-4">
                      <h3 className="text-sm font-medium text-gray-900 mb-2">
                        Key Characteristics:
                      </h3>
                      <ul className="list-disc list-inside space-y-1">
                        {pattern.key_characteristics.map((char, idx) => (
                          <li key={idx} className="text-sm text-gray-600">
                            {char}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  <div className="mt-4 flex items-center text-sm text-gray-500">
                    <span>
                      Added {new Date(pattern.created_at).toLocaleDateString()}
                    </span>
                    {pattern.relevance_score !== null && (
                      <>
                        <span className="mx-2">•</span>
                        <span>
                          Relevance: {(pattern.relevance_score * 100).toFixed(0)}%
                        </span>
                      </>
                    )}
                  </div>
                </div>

                {pattern.relevance_score !== null && (
                  <div className="ml-4 flex-shrink-0">
                    <div className="text-center">
                      <div className="text-3xl font-bold text-blue-600">
                        {(pattern.relevance_score * 10).toFixed(1)}
                      </div>
                      <div className="text-xs text-gray-500">Relevance</div>
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))
        ) : (
          <div className="bg-white shadow rounded-lg p-12 text-center">
            <p className="text-lg text-gray-500 mb-2">No historical patterns yet</p>
            <p className="text-sm text-gray-400">
              Use Claude Code to add historical patterns that provide context for current
              events
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
