import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface Event {
  id: number
  title: string
  description: string
  date: string
  region: string
  impact_level: string
  created_at: string
  updated_at: string
  last_edited_by: string
}

export interface Perspective {
  id: number
  region: string
  summary: string
  key_points: string[]
  language: string | null
  sources: Array<{
    id: number
    title: string
    url: string
  }>
}

export interface EventDetail extends Event {
  perspectives: Perspective[]
}

export interface Metric {
  id: number
  name: string
  description: string | null
  unit: string
  category: string | null
}

export interface MetricDataPoint {
  value: number
  date: string
  notes: string | null
  source_id: number | null
}

export interface Source {
  id: number
  url: string
  title: string
  credibility_tier: string
  region: string | null
  language: string | null
  publisher: string | null
}

export interface Analysis {
  id: number
  title: string
  content: string
  confidence_level: number
  research_approach: string | null
  created_by: string
  created_at: string
}

// Events
export const getEvents = () => api.get<Event[]>('/events')
export const getEvent = (id: number) => api.get<EventDetail>(`/events/${id}`)

// Metrics
export const getMetrics = () => api.get<Metric[]>('/metrics')
export const getMetricHistory = (id: number) =>
  api.get<{ metric: Metric; datapoints: MetricDataPoint[] }>(`/metrics/${id}/history`)

// Sources
export const getSources = (params?: { region?: string; tier?: string }) =>
  api.get<Source[]>('/sources', { params })

// Analyses
export const getAnalyses = () => api.get<Analysis[]>('/analyses')
export const getAnalysis = (id: number) => api.get<Analysis>(`/analyses/${id}`)

// Admin
export const getStats = () =>
  api.get<{
    events: number
    perspectives: number
    sources: number
    analyses: number
    metrics: number
    sources_by_region: Record<string, number>
  }>('/admin/stats')

export default api
