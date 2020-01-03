import { Link } from "gatsby"
import PropTypes from "prop-types"
import React from "react"

const Header = ({ siteTitle }) => (
  <header
    style={{
      background: `#233952`,
      marginBottom: `1.45rem`,
    }}
  >
    <div
      style={{
        margin: `0 auto`,
        maxWidth: 960,
        padding: `1.45rem 1.0875rem`,
      }}
    >
      <h1 style={{ margin: 0, display: "inline" }}>
        <Link
          to="/"
          style={{
            color: `white`,
            textDecoration: `none`,
            textShadow: "2px 2px 8px #000000",
          }}
        >
          {siteTitle}
        </Link>
      </h1>
      <span>
        <Link
          to="/login"
          style={{
            color: `white`,
            textDecoration: `none`,
            textShadow: "2px 2px 8px #000000",
            float: "right",
            marginTop: "0.5rem",
          }}
        >
          Log in
        </Link>
      </span>
      <span>
        <Link
          to="/#about"
          style={{
            color: `white`,
            textDecoration: `none`,
            textShadow: "2px 2px 8px #000000",
            float: "right",
            marginTop: "0.5rem",
            marginRight: "1rem",
          }}
        >
          About
        </Link>
      </span>
      <span>
        <Link
          to="/dashboard"
          style={{
            color: `white`,
            textDecoration: `none`,
            textShadow: "2px 2px 8px #000000",
            float: "right",
            marginTop: "0.5rem",
            marginRight: "1rem",
          }}
        >
          Dashboard
        </Link>
      </span>
    </div>
  </header>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: ``,
}

export default Header
