import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const Dashboard = () => (
  <Layout>
    <SEO title="Dashboard" />
    <h1>Dashboard</h1>
    <Link to="/profile">
      <button style={{
        backgroundColor: '#62799c',
        color: '#fffaff',
        width: '50%',
        height: '100px',
        borderRadius: '25px',
      }}>
        Profile
      </button>
    </Link>

    <Link to="csv-upload">
      <button style={{
        backgroundColor: '#7491bf',
        color: '#fffaff',
        width: '50%',
        height: '100px',
        borderRadius: '25px',
      }}>
        CSV Upload
      </button>
    </Link>

    <a href="http://165.22.191.125:3000/?orgId=1" target="_blank">
      <button style={{
        backgroundColor: '#40577a',
        color: '#fffaff',
        width: '50%',
        height: '100px',
        borderRadius: '25px',
      }}>
        Grafana graphs
      </button>
    </a>

    <Link to="/forms">
      <button style={{
        backgroundColor: '#62799c',
        color: '#fffaff',
        width: '50%',
        height: '100px',
        borderRadius: '25px',
      }}>
        Forms
      </button>
    </Link>
    <Link to="/connect-to-node">
      <button style={{
        backgroundColor: '#62799c',
        color: '#fffaff',
        width: '50%',
        height: '100px',
        borderRadius: '25px',
      }}>
        Connect to node
      </button>
    </Link>
  </Layout >
)

export default Dashboard
