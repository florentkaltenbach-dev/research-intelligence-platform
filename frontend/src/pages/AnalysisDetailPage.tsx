import { useQuery } from '@tanstack/react-query'
import { useParams, Link } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import { getAnalysis } from '../services/api'

export default function AnalysisDetailPage() {
  const { id } = useParams<{ id: string }>()

  const { data: analysis, isLoading, error } = useQuery({
    queryKey: ['analysis', id],
    queryFn: async () => {
      const response = await getAnalysis(Number(id))
      return response.data
    },
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading analysis...</div>
  }

  if (error || !analysis) {
    return (
      <div className="text-center py-12">
        <p className="text-red-600 mb-4">Analysis not found</p>
        <Link to="/analyses" className="text-blue-600 hover:text-blue-800">
          ← Back to Analyses
        </Link>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <Link
          to="/analyses"
          className="text-blue-600 hover:text-blue-800 flex items-center"
        >
          ← Back to Analyses
        </Link>
        <div className="flex items-center">
          {[...Array(5)].map((_, i) => (
            <span key={i} className="text-2xl">
              {i < analysis.confidence_level ? '⭐' : '☆'}
            </span>
          ))}
        </div>
      </div>

      <div className="bg-white shadow rounded-lg p-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">{analysis.title}</h1>

        <div className="flex items-center justify-between text-sm text-gray-500 mb-6 pb-4 border-b">
          <div className="flex flex-col gap-1">
            {analysis.research_approach && (
              <span>
                <strong>Research Approach:</strong> {analysis.research_approach}
              </span>
            )}
            <span>
              <strong>Confidence Level:</strong> {analysis.confidence_level}/5 stars
            </span>
          </div>
          <div className="text-right">
            <div>By {analysis.created_by}</div>
            <div>Created: {new Date(analysis.created_at).toLocaleDateString()}</div>
            <div className="text-xs text-gray-400">
              Updated: {new Date(analysis.updated_at).toLocaleDateString()}
            </div>
          </div>
        </div>

        <div className="prose prose-lg max-w-none">
          <ReactMarkdown>{analysis.content}</ReactMarkdown>
        </div>
      </div>
    </div>
  )
}
