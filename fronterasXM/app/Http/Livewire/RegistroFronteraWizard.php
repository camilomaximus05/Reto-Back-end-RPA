<?php

namespace App\Http\Livewire;

use App\Models\Frontera;
use Livewire\Component;
use Livewire\WithFileUploads;
use Illuminate\Support\Facades\Auth;

class RegistroFronteraWizard extends Component
{
    use WithFileUploads;

    public $paso = 1;

    // Todos los campos del formulario
    public $nombre_solicitante, $fecha_solicitud;
    public $nombre_frontera, $ubicacion;
    public $nombre_usuario, $email_usuario;
    public $tipo_medidor, $serie_medidor;
    public $tipo_curva, $parametros_curva;
    public $certificacion_num, $entidad_certificadora;
    public $archivo_adjunto;

    public function siguientePaso() { $this->paso++; }
    public function pasoAnterior() { if ($this->paso > 1) $this->paso--; }

    public function guardar()
{
    $this->validate([
        'archivo_adjunto' => 'nullable|file|mimes:pdf|max:4096',
    ]);

    $nombreArchivo = null;

    // Solo si el archivo fue cargado correctamente como archivo
    if ($this->archivo_adjunto && $this->archivo_adjunto instanceof \Livewire\TemporaryUploadedFile) {
        $nombreArchivo = $this->archivo_adjunto->store('adjuntos', 'public');
    }

    Frontera::create([
        'user_id' => Auth::id(),
        'nombre_solicitante' => $this->nombre_solicitante,
        'fecha_solicitud' => $this->fecha_solicitud,
        'nombre_frontera' => $this->nombre_frontera,
        'ubicacion' => $this->ubicacion,
        'nombre_usuario' => $this->nombre_usuario,
        'email_usuario' => $this->email_usuario,
        'tipo_medidor' => $this->tipo_medidor,
        'serie_medidor' => $this->serie_medidor,
        'tipo_curva' => $this->tipo_curva,
        'parametros_curva' => $this->parametros_curva,
        'certificacion_num' => $this->certificacion_num,
        'entidad_certificadora' => $this->entidad_certificadora,
        'archivo_adjunto' => $nombreArchivo,
    ]);

    session()->flash('message', 'Archivo subido correctamente.');
    return redirect()->to('/dashboard');
}


    public function render()
    {
        return view('livewire.registro-frontera-wizard');
    }
}
