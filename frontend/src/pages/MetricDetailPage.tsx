import { useQuery } from '@tanstack/react-query'
import { useParams, Link } from 'react-router-dom'
import { getMetricHistory } from '../services/api'
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'

export default function MetricDetailPage() {
  const { id } = useParams<{ id: string }>()

  const { data, isLoading } = useQuery({
    queryKey: ['metric-history', id],
    queryFn: async () => {
      const response = await getMetricHistory(parseInt(id!))
      return response.data
    },
    enabled: !!id,
  })

  if (isLoading) {
    return <div className="text-center py-12">Loading metric data...</div>
  }

  if (!data) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500">Metric not found</p>
        <Link to="/metrics" className="text-blue-600 hover:underline mt-2 inline-block">
          Back to Metrics
        </Link>
      </div>
    )
  }

  const { metric, datapoints } = data

  // Format data for Recharts
  const chartData = datapoints.map((dp) => ({
    date: new Date(dp.date).toLocaleDateString(),
    value: dp.value,
    fullDate: dp.date,
  }))

  // Calculate statistics
  const values = datapoints.map((dp) => dp.value)
  const latestValue = values[values.length - 1]
  const minValue = Math.min(...values)
  const maxValue = Math.max(...values)
  const avgValue = values.reduce((a, b) => a + b, 0) / values.length

  // Calculate trend
  const firstValue = values[0]
  const trend = latestValue - firstValue
  const trendPercent = ((trend / firstValue) * 100).toFixed(2)

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <Link
          to="/metrics"
          className="text-sm text-blue-600 hover:underline mb-2 inline-block"
        >
          ← Back to Metrics
        </Link>
        <h1 className="text-3xl font-bold text-gray-900">{metric.name}</h1>
        <div className="mt-2 flex items-center gap-4 text-sm text-gray-600">
          <span className="font-medium">{metric.category}</span>
          <span>•</span>
          <span>Unit: {metric.unit}</span>
        </div>
      </div>

      {/* Statistics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white shadow rounded-lg p-4">
          <div className="text-sm text-gray-500">Latest Value</div>
          <div className="text-2xl font-bold text-gray-900 mt-1">
            {latestValue.toLocaleString()}
          </div>
          <div className="text-xs text-gray-500 mt-1">{metric.unit}</div>
        </div>

        <div className="bg-white shadow rounded-lg p-4">
          <div className="text-sm text-gray-500">Trend</div>
          <div
            className={`text-2xl font-bold mt-1 ${
              trend >= 0 ? 'text-green-600' : 'text-red-600'
            }`}
          >
            {trend >= 0 ? '+' : ''}
            {trendPercent}%
          </div>
          <div className="text-xs text-gray-500 mt-1">Since first record</div>
        </div>

        <div className="bg-white shadow rounded-lg p-4">
          <div className="text-sm text-gray-500">Range</div>
          <div className="text-lg font-bold text-gray-900 mt-1">
            {minValue.toLocaleString()} - {maxValue.toLocaleString()}
          </div>
          <div className="text-xs text-gray-500 mt-1">Min / Max</div>
        </div>

        <div className="bg-white shadow rounded-lg p-4">
          <div className="text-sm text-gray-500">Average</div>
          <div className="text-2xl font-bold text-gray-900 mt-1">
            {avgValue.toFixed(2).toLocaleString()}
          </div>
          <div className="text-xs text-gray-500 mt-1">{metric.unit}</div>
        </div>
      </div>

      {/* Chart */}
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">Time Series</h2>
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="date"
                tick={{ fontSize: 12 }}
                angle={-45}
                textAnchor="end"
                height={80}
              />
              <YAxis
                tick={{ fontSize: 12 }}
                label={{ value: metric.unit, angle: -90, position: 'insideLeft' }}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: 'white',
                  border: '1px solid #ccc',
                  borderRadius: '4px',
                }}
                formatter={(value: number) => [
                  `${value.toLocaleString()} ${metric.unit}`,
                  'Value',
                ]}
              />
              <Legend />
              <Line
                type="monotone"
                dataKey="value"
                stroke="#3b82f6"
                strokeWidth={2}
                dot={{ fill: '#3b82f6', r: 4 }}
                activeDot={{ r: 6 }}
                name={metric.name}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Data Points Table */}
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">
          Data Points ({datapoints.length})
        </h2>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                  Date
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                  Value
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                  Notes
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {datapoints
                .slice()
                .reverse()
                .map((dp, idx) => (
                  <tr key={idx}>
                    <td className="px-4 py-3 text-sm text-gray-900">
                      {new Date(dp.date).toLocaleDateString()}
                    </td>
                    <td className="px-4 py-3 text-sm font-medium text-gray-900">
                      {dp.value.toLocaleString()} {metric.unit}
                    </td>
                    <td className="px-4 py-3 text-sm text-gray-600">
                      {dp.notes || '-'}
                    </td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
