import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getEvents } from '../services/api'

export default function EventTimelinePage() {
  const { data: events, isLoading } = useQuery({
    queryKey: ['events'],
    queryFn: async () => {
      const response = await getEvents()
      return response.data
    },
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading timeline...</div>
  }

  // Sort events by date (newest first)
  const sortedEvents = events
    ? [...events].sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
    : []

  // Get impact level color
  const getImpactColor = (level: string) => {
    switch (level) {
      case 'critical':
        return 'bg-red-100 text-red-800 border-red-300'
      case 'high':
        return 'bg-orange-100 text-orange-800 border-orange-300'
      case 'medium':
        return 'bg-yellow-100 text-yellow-800 border-yellow-300'
      case 'low':
        return 'bg-green-100 text-green-800 border-green-300'
      default:
        return 'bg-gray-100 text-gray-800 border-gray-300'
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Event Timeline</h1>
        <p className="mt-2 text-gray-600">
          Chronological view of global power transition events
        </p>
      </div>

      {sortedEvents && sortedEvents.length > 0 ? (
        <div className="relative">
          {/* Timeline line */}
          <div className="absolute left-8 top-0 bottom-0 w-0.5 bg-gray-300"></div>

          {/* Events */}
          <div className="space-y-8">
            {sortedEvents.map((event, index) => (
              <div key={event.id} className="relative flex items-start group">
                {/* Timeline dot */}
                <div className="absolute left-8 mt-6 -ml-2 h-4 w-4 rounded-full bg-blue-600 border-4 border-white shadow z-10"></div>

                {/* Event card */}
                <div className="ml-20 flex-1">
                  <Link
                    to={`/events/${event.id}`}
                    className="block bg-white shadow rounded-lg p-6 hover:shadow-xl transition-shadow duration-200"
                  >
                    {/* Date */}
                    <div className="text-sm text-gray-500 mb-2">
                      {new Date(event.date).toLocaleDateString('en-US', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                      })}
                    </div>

                    {/* Title and badges */}
                    <div className="flex items-start justify-between gap-4 mb-3">
                      <h3 className="text-lg font-semibold text-gray-900 group-hover:text-blue-600">
                        {event.title}
                      </h3>
                      <div className="flex gap-2 flex-shrink-0">
                        <span
                          className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border ${getImpactColor(
                            event.impact_level
                          )}`}
                        >
                          {event.impact_level}
                        </span>
                      </div>
                    </div>

                    {/* Region */}
                    <div className="mb-3">
                      <span className="inline-flex items-center text-sm text-gray-600">
                        <svg
                          className="w-4 h-4 mr-1"
                          fill="none"
                          stroke="currentColor"
                          viewBox="0 0 24 24"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                          />
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                          />
                        </svg>
                        {event.region}
                      </span>
                    </div>

                    {/* Description preview */}
                    <p className="text-sm text-gray-600 line-clamp-2">
                      {event.description}
                    </p>

                    {/* View link */}
                    <div className="mt-4 text-sm text-blue-600 group-hover:underline">
                      View details →
                    </div>
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <div className="text-center py-12 bg-white shadow rounded-lg">
          <p className="text-lg text-gray-500 mb-2">No events yet</p>
          <p className="text-sm text-gray-400">
            Use Claude Code to add events to the timeline
          </p>
        </div>
      )}
    </div>
  )
}
