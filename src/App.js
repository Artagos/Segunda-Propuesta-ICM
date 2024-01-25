import ContenedorICM from './Componentes/ContenedoresICM';
import './App.css';

function App() {
  return (
    <div className="App">
<header>
    <h1>Your Website Name</h1>
</header>

<nav>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>

    <ContenedorICM/>
    </div>
  );
}

export default App;
