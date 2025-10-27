import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getEvents } from '../services/api'

export default function EventsPage() {
  const { data: events, isLoading } = useQuery({
    queryKey: ['events'],
    queryFn: async () => {
      const response = await getEvents()
      return response.data
    },
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading events...</div>
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Power Transition Events</h1>
      </div>

      <div className="bg-white shadow rounded-lg divide-y divide-gray-200">
        {events && events.length > 0 ? (
          events.map((event) => (
            <Link
              key={event.id}
              to={`/events/${event.id}`}
              className="block p-6 hover:bg-gray-50 transition"
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <h2 className="text-xl font-semibold text-gray-900 mb-2">{event.title}</h2>
                  <p className="text-gray-600 mb-3 line-clamp-2">{event.description}</p>
                  <div className="flex items-center space-x-4 text-sm text-gray-500">
                    <span>📍 {event.region}</span>
                    <span>📅 {new Date(event.date).toLocaleDateString()}</span>
                    <span>👤 {event.last_edited_by}</span>
                  </div>
                </div>
                <span
                  className={`ml-4 inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${
                    event.impact_level === 'critical'
                      ? 'bg-red-100 text-red-800'
                      : event.impact_level === 'high'
                      ? 'bg-orange-100 text-orange-800'
                      : event.impact_level === 'medium'
                      ? 'bg-yellow-100 text-yellow-800'
                      : 'bg-green-100 text-green-800'
                  }`}
                >
                  {event.impact_level}
                </span>
              </div>
            </Link>
          ))
        ) : (
          <div className="p-12 text-center text-gray-500">
            <p className="text-lg mb-2">No events yet</p>
            <p className="text-sm">Use Claude Code to research and add events</p>
          </div>
        )}
      </div>
    </div>
  )
}
