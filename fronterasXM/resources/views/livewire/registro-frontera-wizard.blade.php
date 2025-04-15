<div class="p-6">
    <h2 class="text-xl font-bold mb-4">Registro de Frontera - Paso {{ $paso }}</h2>

    @if (session()->has('message'))
        <div class="bg-green-100 p-2 rounded mb-4">{{ session('message') }}</div>
    @endif

    <form wire:submit.prevent="{{ $paso === 7 ? 'guardar' : 'siguientePaso' }}" enctype="multipart/form-data">
        @csrf

        @if($paso === 1)
            <!-- Requerimiento -->
            <div>
                <label>Nombre del solicitante:</label>
                <input type="text" wire:model="nombre_solicitante" class="input w-full mb-2">

                <label>Fecha de solicitud:</label>
                <input type="date" wire:model="fecha_solicitud" class="input w-full">
            </div>

        @elseif($paso === 2)
            <!-- Frontera -->
            <div>
                <label>Nombre de la frontera:</label>
                <input type="text" wire:model="nombre_frontera" class="input w-full mb-2">

                <label>Ubicación:</label>
                <input type="text" wire:model="ubicacion" class="input w-full">
            </div>

        @elseif($paso === 3)
            <!-- Usuario -->
            <div>
                <label>Nombre del usuario:</label>
                <input type="text" wire:model="nombre_usuario" class="input w-full mb-2">

                <label>Correo electrónico:</label>
                <input type="email" wire:model="email_usuario" class="input w-full">
            </div>

        @elseif($paso === 4)
            <!-- Equipos de medida -->
            <div>
                <label>Tipo de medidor:</label>
                <input type="text" wire:model="tipo_medidor" class="input w-full mb-2">

                <label>Serie:</label>
                <input type="text" wire:model="serie_medidor" class="input w-full">
            </div>

        @elseif($paso === 5)
            <!-- Curva típica -->
            <div>
                <label>Tipo de curva:</label>
                <input type="text" wire:model="tipo_curva" class="input w-full mb-2">

                <label>Parámetros:</label>
                <textarea wire:model="parametros_curva" class="input w-full"></textarea>
            </div>

        @elseif($paso === 6)
            <!-- Certificaciones -->
            <div>
                <label>Número de certificación:</label>
                <input type="text" wire:model="certificacion_num" class="input w-full mb-2">

                <label>Entidad certificadora:</label>
                <input type="text" wire:model="entidad_certificadora" class="input w-full">
            </div>

            @elseif($paso === 7)
                <div>
                    <label class="block font-semibold mb-1">Archivo adjunto (PDF):</label>
                    <input type="file" wire:model="archivo_adjunto" class="input w-full mb-2" accept="application/pdf">

                    @error('archivo_adjunto') 
                        <span class="text-red-500 text-sm">{{ $message }}</span> 
                    @enderror

                    @if(isset($archivo_adjunto) && is_string($archivo_adjunto))
                        <div class="mt-2">
                            <a href="{{ asset('storage/' . $archivo_adjunto) }}" target="_blank" class="text-blue-600 underline">
                                Ver archivo adjunto existente
                            </a>
                        </div>
                    @endif
                </div>
            @endif


        <!-- Navegación -->
        <div class="mt-6 flex justify-between">
            @if($paso > 1)
                <button type="button" wire:click="pasoAnterior" class="bg-gray-400 hover:bg-gray-500 text-white py-2 px-4 rounded">
                    Atrás
                </button>
            @endif

            <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded">
                {{ $paso === 7 ? 'Guardar' : 'Siguiente' }}
            </button>
        </div>
    </form>
</div>
