
import './App.css';
import Header from './Componentes/header';
import NavBar from './Componentes/Navbar';
import RoutesICM from './Componentes/Routes';
import './ComponentsCss/ContactSection.css'
import './ComponentsCss/Eventos.css'


function App() {
  return (
    <div className="App">
    <Header/>
    <NavBar/>
    <RoutesICM/>
    </div>
  );
}

export default App;
