import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

import YMLData from "../../users.yml"

class CSVUpload extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      username: "",
      password: "",
    }
  }

  handleSubmit = event => {
    event.preventDefault()
    const { username, password } = this.state
    if (username === YMLData.user && password === YMLData.user.password) {
      alert("Logged in")
      // TODO redirect, save a user cookie, and change the Nav to say "Logout"
    }
    alert("Incorrect username and password")
  }

  onChangeHandler = event => {
    const { name, value } = event.target
    const obj = {}
    obj[name] = value
    this.setState(obj)
  }

  render() {
    return (
      <Layout>
        <SEO title="Log in" />
        <h1>Log in</h1>
        <form onSubmit={this.handleSubmit}>
          <div className="field">
            <label htmlFor="username">
              <span className="label">Username</span>
              <br />
            </label>
            <input
              type="text"
              id="username"
              name="username"
              onChange={this.onChangeHandler}
            />
          </div>
          <div className="field">
            <label htmlFor="password">
              <span className="label">Password</span>
              <br />
            </label>
            <input
              type="password"
              id="password"
              name="password"
              onChange={this.onChangeHandler}
            />
          </div>
          <input
            style={{
              backgroundColor: "#7491bf",
              color: "#fffaff",
              width: "220px",
              height: "33px",
              borderRadius: "25px",
              marginTop: "1rem",
            }}
            type="submit"
            value="Upload"
            name="upload"
          />
        </form>
        <Link to="/">Go back to the homepage</Link>
      </Layout>
    )
  }
}

export default CSVUpload
