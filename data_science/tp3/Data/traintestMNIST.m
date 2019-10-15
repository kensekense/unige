function [trainImages, trainLabels, testImages, testLabels] = traintestMNIST(labels, ntrain, ntest)
%traintestMNIST Reads the MNIST datasets.
%
%   [trainImages, trainLabels, testImages, testLabels] = traintestMNIST(labels, ntrain, ntest)
%   Reads the MNIST dataset from the mnist_all.mat file.
%   Then the selection of specific digits is performed according to classes
%   defined in the "labels" variable.
%   It returns "ntrain" and "ntest" randomly selected training and test
%   instance, respectively.
%
%   Input:
%       labels: it is a row vector of integers containing lables to be selected
%           (e.g. labels = [3,4])
%       ntrain: number of training images to be selected. If not given
%           all the training images will be returned
%       ntest: number of test images to be selected. If not given
%           all the test images will be returned
%   Output:
%       trainImages: matrix of row vectors representing training images
%       trainLabels: column vector of training labels
%       testImages: matrix of row vectors representing test images
%       testLabels: column vector of test labels

data=load('mnist_all.mat');

trainImages = zeros(0,784);
testImages = zeros(0,784);
trainLabels = [];
testLabels = [];

for i = 1:size(labels, 2)
    l = strcat( 'train', int2str(labels(i)) );
    tmpTrain = getfield( data, l );
    trainImages = cat( 1, trainImages, tmpTrain );
    trainLabels = cat( 1, trainLabels, labels(i)*ones(size(tmpTrain,1),1) );

    l = strcat( 'test', int2str(labels(i)) );
    tmpTest = getfield( data, l );
    testImages = cat( 1, testImages, tmpTest );
    testLabels = cat( 1, testLabels, labels(i)*ones(size(tmpTest,1),1) );
end

% shuffle the elements
rtrain = randperm( size(trainLabels, 1) );
rtest  = randperm( size(testLabels, 1) );
trainImages = trainImages(rtrain,:);
testImages = testImages(rtest,:);
trainLabels = trainLabels(rtrain);
testLabels = testLabels(rtest);

% if ntrain or ntest is not given return the full set
if nargin > 1
    if size(trainImages, 1) < ntrain
        error('Wrong value of number of training instances')
    end
    trainImages = trainImages(1:ntrain,:);
    trainLabels = trainLabels(1:ntrain);

    if nargin > 2
        if size(testImages, 1) < ntest
            error('Wrong value of number of test instances')
        end
        testImages = testImages(1:ntest,:);
        testLabels = testLabels(1:ntest);
    end
end

trainImages=double(trainImages);
trainLabels=double(trainLabels);
testImages=double(testImages);
testLabels=double(testLabels);
