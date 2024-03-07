import { useState } from 'react'

import '../ComponentsCss/Navbar.css'
import MenuIcon from './MenuIcon'
import React from 'react'
import axios from 'axios'

const Navbar = ({seccion}) => {
  const [showNavbar, setShowNavbar] = useState(false);
  const[iconUrl,setIconUrl]=React.useState('');
  
  const handleShowNavbar = () => {
    setShowNavbar(!showNavbar)
  };
  
  

  React.useEffect(()=>{
    axios.get('http://127.0.0.1:8000/api/entidades/logos')
    .then(response => {
        console.log(response.data);
        console.log(seccion)
        var icons=response.data;
        icons.map((icon)=>{if(icon.seccion===seccion)setIconUrl('/'+icon.foto)
        ()})

    })
    .catch(error => {
      console.error('Error fetching (Logos)', error);
    });
},
[])


  return (
    <nav className="navbar">
      <div className="container">
        <div className="logo" style={{height:'inherit', margin:'20px'}}>
          <img style={{width:"100%", height:"inherit"}} src={"/logos/ICMLOGOBLANCO.png"}></img>
        </div>
        <div className="menu-icon" onClick={handleShowNavbar}>
          <MenuIcon/>
        </div>
        <div className={`nav-elements  ${showNavbar && 'active'}`}>
          <ul>
          <li><a href="/">Principal</a></li>
              <li><a href="Revista">Revista</a></li>
              <li><a href="Eventos">Eventos</a></li>
              <li><a href="Efemerides">Efemerides</a></li>
              <li><a href="Contactos">Contactos</a></li>
              <li><a ></a></li>
              
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar