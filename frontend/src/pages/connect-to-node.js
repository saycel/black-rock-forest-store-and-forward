import React from "react"
import axios from "axios"

import Layout from "../components/layout"
import SEO from "../components/seo"

const NAMESPACE_PREFIX = "BRFP-"
const DATA_PAGE_PREFIX = "data-page-"
class ConnectToNode extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      ipAddress: null,
      message: "",
      dataDownloaded: false,
      downloadInProgress: false,
      finalPage: "",
    }
  }

  handleSubmit = event => {
    event.preventDefault()
    this.getData(this.state.ipAddress)
  }

  saveToLocalStorage(page, data) {
    localStorage.setItem(
      `${NAMESPACE_PREFIX}${DATA_PAGE_PREFIX}${page}`,
      JSON.stringify(data)
    )
  }

  downloadInProgress() {
    this.setState({ downloadInProgress: true })
  }

  finishDownloadInProgress() {
    this.setState({ downloadInProgress: false })
  }

  sendData() {
    const finalPage = parseInt(this.state.finalPage)
    for (let x = 0; x < finalPage; x++) {
      const stringifiedData = localStorage.getItem(
        `${NAMESPACE_PREFIX}${DATA_PAGE_PREFIX}${x}`
      )
      const data = JSON.parse(stringifiedData)
      // how to get data to the server? Can we send it in bulk or
      // are we forced to send it one by one?
    }
  }

  getData = (ipAddress, page = 1, size = 100) => {
    this.downloadInProgress()
    const initialUrl = `http://${ipAddress}:2323/sensor/data/${size}/${page}`
    axios
      .get(initialUrl)
      .then(res => {
        let [h, ...t] = res.data
        this.saveToLocalStorage(page, t)
        this.setState({ dataDownloaded: true })
        const finalPage = h.total_pages
        localStorage.setItem(`${NAMESPACE_PREFIX}finalPage`, finalPage)

        if (page === finalPage) {
          this.setState({ message: "Download complete", finalPage: page })
          this.finishDownloadInProgress()
        } else {
          const nextPage = (page += 1)
          this.setState({
            message: `Downloading page ${nextPage} of ${h.total_pages}`,
            finalPage: nextPage,
          })
          this.getData(ipAddress, nextPage, size)
        }
      })
      .catch(res => {
        this.setState({
          message:
            "Sorry! There was an error. Please contact us to let us know.",
        })
        this.finishDownloadInProgress()
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
        {this.state.dataDownloaded && !this.state.downloadInProgress && (
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
            value="Upload data"
          />
        )}
      </Layout>
    )
  }
}

export default ConnectToNode
