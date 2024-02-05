import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import '../ComponentsCss/Navbar.css'

const Navbar = () => {
  const [showNavbar, setShowNavbar] = useState(false)
console.log(showNavbar)
  const handleShowNavbar = () => {
    setShowNavbar(!showNavbar)
  }

  return (
    <nav className="navbar">
      <div className="container">
        <div className="logo">
          LOGO
        </div>
        <div className="menu-icon" onClick={handleShowNavbar}>
          ICONO
        </div>
        <div className={`nav-elements  ${showNavbar && 'active'}`}>
          <ul>
          <li><a href="/">Principal</a></li>
              <li><a href="Revista">Revista</a></li>
              <li><a href="Eventos">Eventos</a></li>
              <li><a href="Efemerides">Efemerides</a></li>
              <li><a href="Contactos">Contactos</a></li>
              <li><a href="Contactos">Contactos</a></li>
              <li><a href="Contactos">Contactos</a></li>
              <li><a href="Contactos">Contactos</a></li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar