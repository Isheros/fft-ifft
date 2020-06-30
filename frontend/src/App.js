import React from 'react';
import {BrowserRouter as Router, Switch, Route}from 'react-router-dom'

import {Homepage} from './components/Homepage'
import { Navbar } from './components/Navbar'

function App() {
    return(
        <Router>
            <Navbar/>
            <div>
                <Switch>
                    <Route path="/" component={Homepage}/>
                </Switch>
            </div>
        </Router>
    )
}

export default App;
