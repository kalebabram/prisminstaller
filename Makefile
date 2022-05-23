default: dry

dry:
	kubectl apply --recursive --dry-run=client -f ./prism
	kubectl apply --recursive --dry-run=client -f ./posda
	@echo "\nThis was just a dry run, 'make apply' to actually create"
	@echo "Don't forget to create your secrets.yaml, see web/secret.example and coreapi/secret.example for format"

apply:
	kubectl apply --recursive -f ./prism
	kubectl apply --recursive -f ./posda

serve:
	@echo open: http://127.0.0.1.nip.io:8181/
	kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8181:80

status:
	kubectl get all -l prism
