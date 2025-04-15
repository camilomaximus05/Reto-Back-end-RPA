<?php

use Illuminate\Support\Facades\Route;
use App\Http\Livewire\RegistroFronteraWizard;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::middleware([ 
    'auth:sanctum', 
    config('jetstream.auth_session'), 
    'verified' 
])->group(function () {
    Route::get('/dashboard', function () {
        return view('dashboard');
    })->name('dashboard');

    // Ruta para el wizard de frontera
    Route::get('/registro', RegistroFronteraWizard::class)->name('registro');
});

// Redirigir al wizard después del login
Route::get('/', function () {
    return redirect()->route('registro');
});
