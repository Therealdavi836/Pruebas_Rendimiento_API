<?php

namespace App\Http\Controllers;

use App\Models\Product;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class ProductController extends Controller
{
    protected $baseUrl = 'https://fakestoreapi.com/products';

    // GET /products
    public function index()
    {
        $response = Http::get($this->baseUrl);
        return response()->json($response->json());
    }

    // GET /products/{id}
    public function show($id)
    {
        $response = Http::get("{$this->baseUrl}/{$id}");
        return response()->json($response->json());
    }

    // POST /products
    public function store(Request $request)
    {
        $response = Http::post($this->baseUrl, $request->all());
        return response()->json($response->json(), 201);
    }

    // PUT /products/{id}
    public function update(Request $request, $id)
    {
        $response = Http::put("{$this->baseUrl}/{$id}", $request->all());
        return response()->json($response->json());
    }

    // DELETE /products/{id}
    public function destroy($id)
    {
        $response = Http::delete("{$this->baseUrl}/{$id}");
        return response()->json($response->json([
                'message' => 'Producto borrado exitosamente'
            ], 200));
    }
}
