import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getAnalyses } from '../services/api'

export default function AnalysesPage() {
  const { data: analyses, isLoading } = useQuery({
    queryKey: ['analyses'],
    queryFn: async () => {
      const response = await getAnalyses()
      return response.data
    },
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading analyses...</div>
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-gray-900">Research Analyses</h1>

      <div className="space-y-4">
        {analyses && analyses.length > 0 ? (
          analyses.map((analysis) => (
            <div key={analysis.id} className="bg-white shadow rounded-lg p-6">
              <div className="flex justify-between items-start mb-3">
                <h2 className="text-xl font-semibold text-gray-900">{analysis.title}</h2>
                <div className="flex items-center">
                  {[...Array(5)].map((_, i) => (
                    <span key={i} className="text-lg">
                      {i < analysis.confidence_level ? '⭐' : '☆'}
                    </span>
                  ))}
                </div>
              </div>

              <div className="prose max-w-none">
                <p className="text-gray-700 whitespace-pre-wrap line-clamp-3">{analysis.content}</p>
              </div>

              <div className="mt-4 flex items-center justify-between text-sm text-gray-500">
                <span>
                  {analysis.research_approach && `Approach: ${analysis.research_approach}`}
                </span>
                <span>
                  By {analysis.created_by} • {new Date(analysis.created_at).toLocaleDateString()}
                </span>
              </div>

              <div className="mt-4">
                <Link
                  to={`/analyses/${analysis.id}`}
                  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                >
                  View Full Analysis →
                </Link>
              </div>
            </div>
          ))
        ) : (
          <div className="bg-white shadow rounded-lg p-12 text-center text-gray-500">
            <p className="text-lg mb-2">No analyses yet</p>
            <p className="text-sm">
              Use Claude Code to create research analyses and syntheses
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
