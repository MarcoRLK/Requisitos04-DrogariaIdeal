# build node
# Cookbook Name :: build-cookbook
# Recipe:: default

include_recipe 'delivery-truck::default'

docker_instalation 'default' do
    action :create
end

group 'docker' do
    action: create
    members: dbuild
end

docker_service 'default' do
    action[:create, :start]
end
