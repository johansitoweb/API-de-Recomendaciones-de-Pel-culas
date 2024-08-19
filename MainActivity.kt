interface MovieApi {
    @GET("/recommendations")
    suspend fun getRecommendations(): List<String>
}

