import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getEvents } from '../services/api'

const ITEMS_PER_PAGE = 10

export default function EventsPage() {
  const [currentPage, setCurrentPage] = useState(1)

  const { data: response, isLoading } = useQuery({
    queryKey: ['events', currentPage],
    queryFn: async () => {
      const skip = (currentPage - 1) * ITEMS_PER_PAGE
      const result = await getEvents(skip, ITEMS_PER_PAGE)
      return result
    },
  })

  const events = response?.data || []
  const totalEvents = events.length // Backend doesn't return total count, so we estimate

  if (isLoading) {
    return <div className="text-center py-12">Loading events...</div>
  }

  const hasMorePages = events.length === ITEMS_PER_PAGE
  const totalPages = currentPage + (hasMorePages ? 1 : 0)

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Power Transition Events</h1>
        <div className="text-sm text-gray-600">
          Page {currentPage} {hasMorePages && `of ${totalPages}+`}
        </div>
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

      {/* Pagination Controls */}
      {events && events.length > 0 && (
        <div className="bg-white shadow rounded-lg px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex-1 flex justify-between sm:hidden">
              <button
                onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
                disabled={currentPage === 1}
                className={`relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md ${
                  currentPage === 1
                    ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                    : 'bg-white text-gray-700 hover:bg-gray-50'
                }`}
              >
                Previous
              </button>
              <button
                onClick={() => setCurrentPage(currentPage + 1)}
                disabled={!hasMorePages}
                className={`ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md ${
                  !hasMorePages
                    ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                    : 'bg-white text-gray-700 hover:bg-gray-50'
                }`}
              >
                Next
              </button>
            </div>
            <div className="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
              <div>
                <p className="text-sm text-gray-700">
                  Showing page <span className="font-medium">{currentPage}</span>
                  {hasMorePages && ' of many'}
                </p>
              </div>
              <div>
                <nav className="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                  <button
                    onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
                    disabled={currentPage === 1}
                    className={`relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 text-sm font-medium ${
                      currentPage === 1
                        ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                        : 'bg-white text-gray-500 hover:bg-gray-50'
                    }`}
                  >
                    <span className="sr-only">Previous</span>
                    <svg className="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                      <path fillRule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  </button>

                  {/* Current page indicator */}
                  <span className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-blue-50 text-sm font-medium text-blue-600">
                    {currentPage}
                  </span>

                  {hasMorePages && (
                    <>
                      <button
                        onClick={() => setCurrentPage(currentPage + 1)}
                        className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50"
                      >
                        {currentPage + 1}
                      </button>
                      <span className="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
                        ...
                      </span>
                    </>
                  )}

                  <button
                    onClick={() => setCurrentPage(currentPage + 1)}
                    disabled={!hasMorePages}
                    className={`relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 text-sm font-medium ${
                      !hasMorePages
                        ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                        : 'bg-white text-gray-500 hover:bg-gray-50'
                    }`}
                  >
                    <span className="sr-only">Next</span>
                    <svg className="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                      <path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd" />
                    </svg>
                  </button>
                </nav>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
