clear
clc
format long

fprintf('START - %s\n',datetime(now,'ConvertFrom','datenum'));

% parameters
N = 2; % the choosed dimension

u = zeros(N,1);
u(randi(N)) = 1;% random canonic vector of dimension N
v = rand(N,1); % random vector of dimension N

w = deviate_vector(u, v); % w is a vector, function of u and v based on some geometrics

fprintf('Result = %s\n', num2str(round(scalar_product(u, w),1)));

fprintf('END - %s\n', datetime(now,'ConvertFrom','datenum'));

% USED FUNCTIONS AT THE END :
function s = scalar_product(u, v)
% takes a pair of vectors (u, v) as input and returns their scalar product
% such that s = sum_{i=1..N}(u_i * v_i)

s = sum(u .* v);
end

function w = deviate_vector(u, v)
% takes a pair of vectors (u, v) as input and returns a vector w defined by
% w = v - projection of v on u.

w = v - project_on_first(u, v);
end

function w = project_on_first(u, v)
% takes a pair of vectors (u, v) as input and returns the vector w which is
% the projection of v on u : w and u are colinear. All vectors are column!
% subspace is a build-in function of matlab which returns the angle between
% 2 column vectors.

w = norm(v) * cos(subspace(u, v)) * u;
end