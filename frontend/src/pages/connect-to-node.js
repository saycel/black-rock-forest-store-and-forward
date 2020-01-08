import React from "react"
import axios from "axios"

import Layout from "../components/layout"
import SEO from "../components/seo"

class ConnectToNode extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      ipAddress: null,
      message: "",
    }
  }

  handleSubmit = event => {
    event.preventDefault()
    this.getData(this.state.ipAddress)
  }

  saveToLocalStorage(page, data) {
    localStorage.setItem(page, JSON.stringify(data))
  }

  getData = (ipAddress, page = 1, size = 100) => {
    localStorage.setItem("downloadInProgress", "true")
    let initialUrl = `http://${ipAddress}:2323/sensor/data/${size}/${page}`
    axios
      .get(initialUrl)
      .then(res => {
        // then print response status
        let [h, ...t] = res.data
        this.saveToLocalStorage(page, t)
        const finalPage = h.total_pages
        localStorage.setItem("finalPage", finalPage)

        if (page === finalPage) {
          this.setState({ message: "Download complete" })
          localStorage.removeItem("downloadInProgress")
        } else {
          const nextPage = (page += 1)
          this.setState({
            message: `Downloading page ${nextPage} of ${h.total_pages}`,
          })
          this.getData(ipAddress, nextPage, size)
        }
      })
      .catch(res => {
        this.setState({
          message:
            "Sorry! There was an error. Please contact us to let us know.",
        })
      })
  }
  handleChange = event => {
    this.setState({
      ipAddress: event.target.value,
    })
  }

  render() {
    return (
      <Layout>
        <SEO title="Connect to node" />
        <h1>Connect to node</h1>
        <span>{this.state.message}</span>
        <form onSubmit={this.handleSubmit}>
          <div className="addAnother">
            <div className="addAnother-item">
              <div className="field">
                <label htmlFor="items[0][description]">
                  <span className="field-label">Node ip address</span>
                  <br />
                </label>
                <input
                  type="text"
                  id="ipAddress"
                  name="ipAddress"
                  onChange={this.handleChange}
                />
              </div>
            </div>
          </div>
          <br />
          <input
            style={{
              backgroundColor: "#62799c",
              color: "#fffaff",
              width: "196px",
              height: "33px",
              borderRadius: "25px",
            }}
            type="submit"
            name="submit"
            value="Submit"
          />
        </form>
      </Layout>
    )
  }
}

export default ConnectToNode
