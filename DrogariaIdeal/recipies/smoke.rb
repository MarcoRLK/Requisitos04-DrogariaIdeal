adddress=node['ipaddress']

execute "cURL #{address} and verify 200 response" do
    command "curl -IL #{address} | grep '^HTTP/1\.1 200 ok'"
end
