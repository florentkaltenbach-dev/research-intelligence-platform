import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { useParams, Link } from 'react-router-dom'
import { getEvent } from '../services/api'

const INITIAL_PERSPECTIVES_SHOW = 3

export default function EventDetailPage() {
  const { id } = useParams<{ id: string }>()
  const [showAllPerspectives, setShowAllPerspectives] = useState(false)

  const { data: event, isLoading } = useQuery({
    queryKey: ['event', id],
    queryFn: async () => {
      const response = await getEvent(Number(id))
      return response.data
    },
    enabled: !!id,
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading event...</div>
  }

  if (!event) {
    return <div className="text-center py-12">Event not found</div>
  }

  const perspectives = event.perspectives || []
  const displayedPerspectives = showAllPerspectives
    ? perspectives
    : perspectives.slice(0, INITIAL_PERSPECTIVES_SHOW)
  const hasMorePerspectives = perspectives.length > INITIAL_PERSPECTIVES_SHOW

  return (
    <div className="space-y-6">
      <Link to="/events" className="text-blue-600 hover:text-blue-800 text-sm">
        ← Back to Events
      </Link>

      {/* Event Header */}
      <div className="bg-white shadow rounded-lg p-6">
        <div className="flex justify-between items-start mb-4">
          <h1 className="text-3xl font-bold text-gray-900">{event.title}</h1>
          <span
            className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${
              event.impact_level === 'critical'
                ? 'bg-red-100 text-red-800'
                : event.impact_level === 'high'
                ? 'bg-orange-100 text-orange-800'
                : event.impact_level === 'medium'
                ? 'bg-yellow-100 text-yellow-800'
                : 'bg-green-100 text-green-800'
            }`}
          >
            {event.impact_level} impact
          </span>
        </div>

        <div className="flex items-center space-x-4 text-sm text-gray-500 mb-4">
          <span>📍 {event.region}</span>
          <span>📅 {new Date(event.date).toLocaleDateString()}</span>
          <span>👤 {event.last_edited_by}</span>
        </div>

        <p className="text-gray-700 text-lg leading-relaxed">{event.description}</p>
      </div>

      {/* Perspectives */}
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">
          Regional Perspectives ({perspectives.length})
        </h2>

        {perspectives.length > 0 ? (
          <div className="space-y-6">
            {displayedPerspectives.map((perspective) => (
              <div key={perspective.id} className="border-l-4 border-blue-500 pl-4">
                <div className="flex items-center space-x-2 mb-2">
                  <h3 className="text-lg font-semibold text-gray-900">{perspective.region}</h3>
                  {perspective.language && (
                    <span className="text-sm text-gray-500">({perspective.language})</span>
                  )}
                </div>

                <p className="text-gray-700 mb-3">{perspective.summary}</p>

                {perspective.key_points && perspective.key_points.length > 0 && (
                  <div className="mb-3">
                    <p className="text-sm font-medium text-gray-700 mb-1">Key Points:</p>
                    <ul className="list-disc list-inside space-y-1">
                      {perspective.key_points.map((point, idx) => (
                        <li key={idx} className="text-sm text-gray-600">
                          {point}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {perspective.sources && perspective.sources.length > 0 && (
                  <div>
                    <p className="text-sm font-medium text-gray-700 mb-1">Sources:</p>
                    <div className="space-y-1">
                      {perspective.sources.map((source) => (
                        <a
                          key={source.id}
                          href={source.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="block text-sm text-blue-600 hover:text-blue-800"
                        >
                          {source.title} →
                        </a>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ))}

            {/* Show More Button */}
            {hasMorePerspectives && !showAllPerspectives && (
              <div className="text-center pt-4">
                <button
                  onClick={() => setShowAllPerspectives(true)}
                  className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                >
                  Show {perspectives.length - INITIAL_PERSPECTIVES_SHOW} more perspective
                  {perspectives.length - INITIAL_PERSPECTIVES_SHOW !== 1 ? 's' : ''}
                </button>
              </div>
            )}

            {/* Show Less Button */}
            {showAllPerspectives && hasMorePerspectives && (
              <div className="text-center pt-4">
                <button
                  onClick={() => setShowAllPerspectives(false)}
                  className="inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                >
                  Show less
                </button>
              </div>
            )}
          </div>
        ) : (
          <p className="text-gray-500 text-center py-8">
            No perspectives yet. Use Claude Code to add regional viewpoints!
          </p>
        )}
      </div>
    </div>
  )
}
