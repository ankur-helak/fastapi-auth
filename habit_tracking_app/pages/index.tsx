import Layout from '../components/Layout'

const IndexPage = () => (
  <Layout title="Home | Habit Tracker">
    <div className="container mx-auto px-4">
      <h1 className="text-3xl font-bold text-gray-900 mb-4">Welcome to Habit Tracker</h1>
      <p className="text-lg text-gray-600">Start tracking your habits today and achieve your goals!</p>
    </div>
  </Layout>
)

export default IndexPage
