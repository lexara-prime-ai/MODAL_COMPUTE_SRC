use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn square_as_string(a: usize) -> PyResult<String> {
    Ok((a * a).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn modal_compute(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(square_as_string, m)?)?;
    Ok(())
}



