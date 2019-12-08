import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"

const ConnectToNode = () => (
  <Layout>
    <SEO title="Connect to node" />
    <h1>Connect to node</h1>

    <form>
      <div class="addAnother">
        <div class="addAnother-item">
          <div class="field">
            <label for="items[0][description]">
              <span class="field-label">Node ip address</span>
              <br />
            </label>
            <input
              type="text"
              id="items[0][description]"
              name="items[0][description]" />
          </div>
        </div>
      </div>
      <br />
      <input style={{
        backgroundColor: '#62799c',
        color: '#fffaff',
        width: '196px',
        height: '33px',
        borderRadius: '25px',
      }} type="submit" name="submit" value="Submit" />
    </form>
  </Layout >
)

export default ConnectToNode
