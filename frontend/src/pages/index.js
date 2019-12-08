import React from "react"

import Layout from "../components/layout"
import HeroImage from "../components/heroImage"
import TeamImage from "../components/teamImage"

import SEO from "../components/seo"

const IndexPage = () => (
  <Layout>
    <SEO title="Home" />
    <div style={{ maxWidth: `1200px`, marginBottom: `1.45rem` }}>
      <HeroImage />
    </div>
    <div id="about" style={{ maxWidth: `1200px`, marginBottom: `1.45rem` }}>
      <h1>
        About us
      </h1>
      <TeamImage />
      <p>Text about Saycel.com and The Black Rock Forest Project goes here.</p>
    </div>
  </Layout>
)

export default IndexPage
