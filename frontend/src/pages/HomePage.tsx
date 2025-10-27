import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getEvents, getStats } from '../services/api'
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts'

export default function HomePage() {
  const { data: events } = useQuery({
    queryKey: ['events'],
    queryFn: async () => {
      const response = await getEvents()
      return response.data
    },
  })

  const { data: stats } = useQuery({
    queryKey: ['stats'],
    queryFn: async () => {
      const response = await getStats()
      return response.data
    },
  })

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="bg-white rounded-lg shadow p-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Research Intelligence Platform
        </h1>
        <p className="text-lg text-gray-600">
          Analyzing global power transitions and capital flows through multi-perspective research
        </p>
      </div>

      {/* Stats Grid */}
      {stats && (
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
          <div className="bg-white overflow-hidden shadow rounded-lg">
            <div className="p-5">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <div className="text-3xl">📅</div>
                </div>
                <div className="ml-5 w-0 flex-1">
                  <dl>
                    <dt className="text-sm font-medium text-gray-500 truncate">Events</dt>
                    <dd className="text-2xl font-semibold text-gray-900">{stats.events}</dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white overflow-hidden shadow rounded-lg">
            <div className="p-5">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <div className="text-3xl">🌍</div>
                </div>
                <div className="ml-5 w-0 flex-1">
                  <dl>
                    <dt className="text-sm font-medium text-gray-500 truncate">Perspectives</dt>
                    <dd className="text-2xl font-semibold text-gray-900">{stats.perspectives}</dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white overflow-hidden shadow rounded-lg">
            <div className="p-5">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <div className="text-3xl">📚</div>
                </div>
                <div className="ml-5 w-0 flex-1">
                  <dl>
                    <dt className="text-sm font-medium text-gray-500 truncate">Sources</dt>
                    <dd className="text-2xl font-semibold text-gray-900">{stats.sources}</dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white overflow-hidden shadow rounded-lg">
            <div className="p-5">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <div className="text-3xl">📊</div>
                </div>
                <div className="ml-5 w-0 flex-1">
                  <dl>
                    <dt className="text-sm font-medium text-gray-500 truncate">Analyses</dt>
                    <dd className="text-2xl font-semibold text-gray-900">{stats.analyses}</dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Geographic Distribution */}
      {stats && events && events.length > 0 && (
        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">
            Geographic Distribution of Events
          </h2>
          <div className="h-80">
            {(() => {
              // Count events by region
              const regionCounts: { [key: string]: number } = {}
              events.forEach((event) => {
                regionCounts[event.region] = (regionCounts[event.region] || 0) + 1
              })

              // Convert to chart data
              const chartData = Object.entries(regionCounts).map(([region, count]) => ({
                name: region,
                value: count,
              }))

              // Colors for chart
              const COLORS = [
                '#3b82f6', // blue
                '#10b981', // green
                '#f59e0b', // amber
                '#ef4444', // red
                '#8b5cf6', // purple
                '#ec4899', // pink
                '#06b6d4', // cyan
                '#f97316', // orange
              ]

              return (
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={chartData}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, percent }) =>
                        `${name} (${(percent * 100).toFixed(0)}%)`
                      }
                      outerRadius={100}
                      fill="#8884d8"
                      dataKey="value"
                    >
                      {chartData.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={COLORS[index % COLORS.length]}
                        />
                      ))}
                    </Pie>
                    <Tooltip />
                    <Legend />
                  </PieChart>
                </ResponsiveContainer>
              )
            })()}
          </div>
        </div>
      )}

      {/* Recent Events */}
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Recent Events</h2>
        <div className="space-y-4">
          {events && events.length > 0 ? (
            events.slice(0, 5).map((event) => (
              <Link
                key={event.id}
                to={`/events/${event.id}`}
                className="block p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition"
              >
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="text-lg font-semibold text-gray-900">{event.title}</h3>
                    <p className="text-sm text-gray-600 mt-1">
                      {event.region} • {new Date(event.date).toLocaleDateString()}
                    </p>
                  </div>
                  <span
                    className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
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
            <p className="text-gray-500 text-center py-8">
              No events yet. Use Claude Code to add research!
            </p>
          )}
        </div>
        {events && events.length > 5 && (
          <div className="mt-4 text-center">
            <Link to="/events" className="text-blue-600 hover:text-blue-800 font-medium">
              View all events →
            </Link>
          </div>
        )}
      </div>
    </div>
  )
}
