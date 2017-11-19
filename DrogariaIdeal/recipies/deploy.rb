container = "infra-docker-#{delivery_environment}"

execute 'start_chef_client' do
    command "docker exec #{container} chef client --runlist 'recipe[sitebadass]' -E #{delivery_environment} -N #{container}" 
end
