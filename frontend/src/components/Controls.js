import React from 'react'


export const Controls = () => {

    const handleSumbit = async (e) => {
        e.preventDefault();
        const sec = document.getElementById('secuencia').value;
        const ope = document.getElementById('operacion').value;
        const res = await fetch(`https://fft-calculator.herokuapp.com/api/calculate`, {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ope,
                sec
            })
        })
        const data = await res.json();
        document.getElementById('resultado').value = data;
        console.log(data)
    }

    return (
        <form onSubmit={handleSumbit}>
            <fieldset>
                <legend>Calculadora FFT/IFFT</legend>
                <div className="form-group">
                    <label htmlFor="operacion">Operacion:</label>
                    <select className="form-control" id="operacion">
                        <option>FFT</option>
                        <option>IFFT</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="secuencia">Secuencia de entrada</label>
                    <input className="form-control" id="secuencia" placeholder="2,2,2,2*,2,2" />
                </div>
                <button type="submit" className="btn btn-outline-primary">Calcular :)</button>
                <div className="form-group">
                    <label htmlFor="resultado">Resultado </label>
                    <input className="form-control" id="resultado" disabled/>
                </div>
            </fieldset>
        </form>
    )
}