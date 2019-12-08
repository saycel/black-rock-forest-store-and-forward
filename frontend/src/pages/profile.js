import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"

const Profile = () => (
  <Layout>
    <SEO title="Profile" />
    <h1>Profile</h1>

    <form>
      <div class="addAnother">
        <div class="addAnother-item">
          <div class="field">
            <label for="items[0][description]">
              <span class="field-label">Name</span>
              <br />
            </label>
            <input
              type="text"
              id="items[0][description]"
              name="items[0][description]" />
          </div>
          <div class="field">
            <label for="items[0][amount]">
              <span class="field-label">Job title</span>
            </label>
            <br />
            <input
              type="text"
              id="items[0][amount]"
              name="items[0][amount]" />
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

export default Profile
