class PokedexBySpeed(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        speed_lower = self.request.query_params.get('speed_lower', None)
        speed_upper = self.request.query_params.get('speed_upper', None)
        speed_equal = self.request.query_params.get('speed_equal', None)

        if speed_lower is not None:
            queryset = queryset.filter(speed__lt=speed_lower)
        if speed_upper is not None:
            queryset = queryset.filter(speed__gt=speed_upper)
        if speed_equal is not None:
            queryset = queryset.filter(speed=speed_equal)

        return queryset