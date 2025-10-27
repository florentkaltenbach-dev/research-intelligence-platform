import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getMetrics } from '../services/api'

export default function MetricsPage() {
  const { data: metrics, isLoading } = useQuery({
    queryKey: ['metrics'],
    queryFn: async () => {
      const response = await getMetrics()
      return response.data
    },
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading metrics...</div>
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-gray-900">Tracked Metrics</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {metrics && metrics.length > 0 ? (
          metrics.map((metric) => (
            <Link
              key={metric.id}
              to={`/metrics/${metric.id}`}
              className="bg-white shadow rounded-lg p-5 hover:shadow-lg transition-shadow duration-200 block"
            >
              <h3 className="text-lg font-semibold text-gray-900 mb-2">{metric.name}</h3>
              {metric.description && (
                <p className="text-sm text-gray-600 mb-3">{metric.description}</p>
              )}
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-500">{metric.category}</span>
                <span className="text-sm font-medium text-blue-600">{metric.unit}</span>
              </div>
              <div className="mt-3 text-sm text-blue-600 hover:underline">
                View time series →
              </div>
            </Link>
          ))
        ) : (
          <div className="col-span-full text-center py-12 text-gray-500">
            <p className="text-lg mb-2">No metrics yet</p>
            <p className="text-sm">Use Claude Code to start tracking financial indicators</p>
          </div>
        )}
      </div>
    </div>
  )
}
