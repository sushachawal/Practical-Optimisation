function op = schwefel(x)
    op = sum(-x.*sin(sqrt(abs(x))));
end