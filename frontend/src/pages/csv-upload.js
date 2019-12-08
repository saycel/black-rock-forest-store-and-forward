import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const CSVUpload = () => (
  <Layout>
    <SEO title="CSV Upload" />
    <h1>CSV Upload</h1>
    <form
      encType="multipart/form-data"
      method="PUT"
      action="165.22.191.125:2323/data_uploader/data"
    >
      <div className="field">
        <label htmlFor="documents">
          <span className="label">Choose a csv to upload</span>
          <br />
        </label>
        <input className="field-file" type="file" id="file" name="file" />
      </div>
      <input style={{
        backgroundColor: '#7491bf',
        color: '#fffaff',
        width: '220px',
        height: '33px',
        borderRadius: '25px',
        marginTop: '1rem',
      }}
        type="submit" value="Upload" name="upload" />
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout >
)

export default CSVUpload
