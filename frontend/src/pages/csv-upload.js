import React from "react"
import { Link } from "gatsby"
import axios from 'axios';

import Layout from "../components/layout"
import SEO from "../components/seo"

class CSVUpload extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      file: null
    }
  }

  handleSubmit = event => {
    event.preventDefault()
    console.log(this.state)
    const data = new FormData();
    data.append('file', this.state.file)
    axios.put("http://165.22.191.125:2323/data_uploader/data", data, { // receive two parameter endpoint url ,form data 
    })
      .then(res => { // then print response status
        console.log(res.statusText)
        alert("Form submitted!");
      })
      .catch(res => {
        console.log(res)
        alert("Sorry! There was an error. Please click the 'Contact' link to let us know.");
      })
  }

  onChangeHandler = event => {
    this.setState({
      file: event.target.files[0],
      loaded: 0,
    })
  }

  render() {
    return <Layout>
      <SEO title="CSV Upload" />
      <h1>CSV Upload</h1>
      <form
        onSubmit={this.handleSubmit}
        encType="multipart/form-data"
      >
        <div className="field">
          <label htmlFor="documents">
            <span className="label">Choose a csv to upload</span>
            <br />
          </label>
          <input
            className="field-file"
            type="file"
            id="file"
            name="file"
            onChange={this.onChangeHandler}
          />
        </div>
        <input style={{
          backgroundColor: '#7491bf',
          color: '#fffaff',
          width: '220px',
          height: '33px',
          borderRadius: '25px',
          marginTop: '1rem',
        }}
          type="submit"
          value="Upload"
          name="upload"
        />
      </form>
      <Link to="/">Go back to the homepage</Link>
    </Layout >
  }
}

export default CSVUpload
