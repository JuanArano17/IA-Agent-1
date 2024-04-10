from crewai_tools import BaseTool
from pydantic import Field
import os
import requests

class BCRATool(BaseTool):
    # Definir name y description como atributos de clase si son constantes
    name: str = "BCRATool"
    api_key: str = os.getenv("BCRA_API_KEY")
    description: str = """Herramienta para consultar datos económicos del BCRA.
    https://api.estadisticasbcra.com/milestones : eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)
    https://api.estadisticasbcra.com/base : base monetaria
    https://api.estadisticasbcra.com/base_usd: base monetaria dividida USD
    https://api.estadisticasbcra.com/usd : cotización del USD
    https://api.estadisticasbcra.com/usd_of : cotización del USD Oficial
    https://api.estadisticasbcra.com/usd_of_minorista : cotización del USD Oficial (Minorista)
    https://api.estadisticasbcra.com/var_usd_vs_usd_of : porcentaje de variación entre la cotización del USD y el USD oficial
    https://api.estadisticasbcra.com/circulacion_monetaria : circulación monetaria
    https://api.estadisticasbcra.com/billetes_y_monedas : billetes y monedas
    https://api.estadisticasbcra.com/efectivo_en_ent_fin : efectivo en entidades financieras
    https://api.estadisticasbcra.com/depositos_cuenta_ent_fin : depositos de entidades financieras en cuenta del BCRA
    https://api.estadisticasbcra.com/plazo_fijo : plazos fijos
    https://api.estadisticasbcra.com/tasa_depositos_30_dias : tasa de interés por depósitos
    /////
    https://api.estadisticasbcra.com/porc_prestamos_vs_depositos : porcentaje de prestamos en relación a depósitos
    https://api.estadisticasbcra.com/lebac : LEBACs
    https://api.estadisticasbcra.com/leliq : LELIQs
    https://api.estadisticasbcra.com/lebac_usd : LEBACs en USD
    https://api.estadisticasbcra.com/leliq_usd : LELIQs en USD
    https://api.estadisticasbcra.com/leliq_usd_of : LELIQs en USD Oficial
    https://api.estadisticasbcra.com/tasa_leliq : Tasa de LELIQs
    https://api.estadisticasbcra.com/m2_privado_variacion_mensual : M2 privado variación mensual
    https://api.estadisticasbcra.com/cer : CER
    https://api.estadisticasbcra.com/uva : UVA
    https://api.estadisticasbcra.com/uvi : UVI
    https://api.estadisticasbcra.com/tasa_badlar : tasa BADLAR
    https://api.estadisticasbcra.com/tasa_baibar : tasa BAIBAR
    https://api.estadisticasbcra.com/tasa_tm20 : tasa TM20
    https://api.estadisticasbcra.com/tasa_pase_activas_1_dia : tasa pase activas a 1 día
    https://api.estadisticasbcra.com/tasa_pase_pasivas_1_dia : tasa pase pasivas a 1 día
    https://api.estadisticasbcra.com/inflacion_mensual_oficial : inflación mensual oficial
    https://api.estadisticasbcra.com/inflacion_interanual_oficial : inflación inteanual oficial
    https://api.estadisticasbcra.com/inflacion_esperada_oficial : inflación esperada oficial
    https://api.estadisticasbcra.com/dif_inflacion_esperada_vs_interanual : diferencia entre inflación interanual oficial y esperada
    https://api.estadisticasbcra.com/var_base_monetaria_interanual : variación base monetaria interanual
    https://api.estadisticasbcra.com/var_usd_interanual : variación USD interanual
    https://api.estadisticasbcra.com/var_usd_oficial_interanual : variación USD (Oficial) interanual
    https://api.estadisticasbcra.com/var_merval_interanual : variación merval interanual
    https://api.estadisticasbcra.com/var_usd_anual : variación anual del dólar (porcentaje de variación de la cotización del dólar un año despues a la cotización de la fecha indicada)
    https://api.estadisticasbcra.com/var_usd_of_anual : variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada)
    https://api.estadisticasbcra.com/var_merval_anual : variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)
    https://api.estadisticasbcra.com/merval : MERVAL
    https://api.estadisticasbcra.com/merval_usd : MERVAL dividido cotización del USD
    """

    def _run(self, endpoint: str, *args, **kwargs) -> str:
        base_url = "https://api.estadisticasbcra.com"
        url = f"{base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            response = requests.get(url, headers=headers)
            return response.json()
        except Exception as e:
            return f"Error al acceder a los datos del BCRA: {e}"
