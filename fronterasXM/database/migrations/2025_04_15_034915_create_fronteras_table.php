<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */

    public function up()
    {
        Schema::create('fronteras', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
    
            // Paso 1: Requerimiento
            $table->string('nombre_solicitante')->nullable();
            $table->date('fecha_solicitud')->nullable();
    
            // Paso 2: Frontera
            $table->string('nombre_frontera')->nullable();
            $table->string('ubicacion')->nullable();
    
            // Paso 3: Usuario
            $table->string('nombre_usuario')->nullable();
            $table->string('email_usuario')->nullable();
    
            // Paso 4: Equipos
            $table->string('tipo_medidor')->nullable();
            $table->string('serie_medidor')->nullable();
    
            // Paso 5: Curva típica
            $table->string('tipo_curva')->nullable();
            $table->text('parametros_curva')->nullable();
    
            // Paso 6: Certificaciones
            $table->string('certificacion_num')->nullable();
            $table->string('entidad_certificadora')->nullable();
    
            // Paso 7: Adjuntos (solo guardar nombre de archivo por ahora)
            $table->string('archivo_adjunto')->nullable();

    
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('fronteras');
    }
};
