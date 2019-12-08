import React from "react"
import axios from 'axios';

import Layout from "../components/layout"
import SEO from "../components/seo"

class ConnectToNode extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      ipAddress: null
    }
  }

  handleSubmit = event => {
    event.preventDefault()
    this.getData(this.state.ipAddress)
    console.log('submit', this.state)
  }

  getData = (ipAddress, page = 1, size = 10, totalLoaded = 0) => {
    let initialUrl = `http://${ipAddress}:2323/sensor/data/${size}/${page}`;
    axios.get(initialUrl, {
      headers: {
        'Access-Control-Allow-Origin': '*',
      }
    })
      .then(res => { // then print response status
        console.log(res)
        alert("Form submitted!");
      })
      .catch(res => {
        console.log(res)
        alert("Sorry! There was an error. Please click the 'Contact' link to let us know.");
      })

  }
  handleChange = event => {
    this.setState({
      ipAddress: event.target.value
    })
  }

  render() {
    return <Layout>
      <SEO title="Connect to node" />
      <h1>Connect to node</h1>

      <form onSubmit={this.handleSubmit}>
        <div class="addAnother">
          <div class="addAnother-item">
            <div class="field">
              <label for="items[0][description]">
                <span class="field-label">Node ip address</span>
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
        <input style={{
          backgroundColor: '#62799c',
          color: '#fffaff',
          width: '196px',
          height: '33px',
          borderRadius: '25px',
        }} type="submit" name="submit" value="Submit" />
      </form>
    </Layout >
  }
}


export default ConnectToNode;
