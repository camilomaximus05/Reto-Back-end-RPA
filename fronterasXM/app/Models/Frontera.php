<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Frontera extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id',
        'nombre_solicitante',
        'fecha_solicitud',
        'nombre_frontera',
        'ubicacion',
        'nombre_usuario',
        'email_usuario',
        'tipo_medidor',
        'serie_medidor',
        'tipo_curva',
        'parametros_curva',
        'certificacion_num',
        'entidad_certificadora',
        'archivo_adjunto',
    ];
}
