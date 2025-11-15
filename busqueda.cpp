#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <cstdint>

namespace py = pybind11;

// Función auxiliar para obtener un bit de un buffer binario
inline bool getBit(const std::vector<uint8_t>& buffer, size_t bitIndex) {
    size_t byteIndex = bitIndex / 8;
    size_t offset = 7 - (bitIndex % 8); // MSB primero
    return (buffer[byteIndex] >> offset) & 1;
}

// Buscar patrón binario dentro de un buffer
std::vector<int> buscar_patron_binario(const std::vector<uint8_t>& data,
                                       const std::vector<uint8_t>& pattern,
                                       size_t patternBits) {
    std::vector<int> posiciones;
    size_t dataBits = data.size() * 8;

    for (size_t i = 0; i + patternBits <= dataBits; i++) {
        bool match = true;
        for (size_t j = 0; j < patternBits; j++) {
            if (getBit(data, i + j) != getBit(pattern, j)) {
                match = false;
                break;
            }
        }
        if (match) posiciones.push_back(i);
    }
    return posiciones;
}

PYBIND11_MODULE(busqueda, m) {
    m.def("buscar_patron_binario", &buscar_patron_binario,
          "Busca un patrón binario dentro de un buffer",
          py::arg("data"), py::arg("pattern"), py::arg("patternBits"));
}
