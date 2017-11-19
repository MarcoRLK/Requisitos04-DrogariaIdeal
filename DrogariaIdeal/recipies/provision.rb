include_recipe 'delivery-truck::provision'

include_recipe 'build-cookbook::cleanenv'

container = "infra-docker-#{delivery_environment}"

docker_image 'mfdii/ubuntu-systemd' do
    action :pull
    tag 'latest'
end

docker_container container do
    repo 'mfdii/ubuntu-systemd'
    privilege true
    port '80:80'
    extra_hosts ['cad-chef-server:172.31.54.57']
end
