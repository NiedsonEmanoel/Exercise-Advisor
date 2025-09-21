import streamlit as st

st.set_page_config(page_title="Anamnese - Exercise Advisor", page_icon="📋", layout="centered")

# =======================
# Comentários e explicações
# =======================
# Este código utiliza st.tabs para criar uma navegação simples e direta.
# Os dados de cada aba são salvos diretamente no st.session_state,
# o que garante que as informações não se percam ao navegar entre as abas.
# Foram adicionadas seções de saúde para uma anamnese mais completa.

# =======================
# Definição das abas
# =======================
tab_labels = [
    "🧑 Identificação",
    "❤️ Saúde e Estilo de Vida",
    "📏 Antropométricos",
    "💪 Simetria Muscular",
    "🎯 Objetivos e Experiência",
    "✅ Resumo Completo"
]

tabs = st.tabs(tab_labels)


# =======================
# PÁGINA 1 - Identificação
# =======================
with tabs[0]:
    st.title("📋 Anamnese - Identificação")
    st.markdown("### Informe seus dados pessoais")

    # Armazenar os dados no session_state para persistir entre as abas
    st.session_state.nome = st.text_input("Nome", value=st.session_state.get("nome", ""))
    st.session_state.idade = st.number_input("Idade", min_value=12, max_value=100, step=1, value=st.session_state.get("idade", 18))
    st.session_state.sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"], index=["Masculino", "Feminino", "Outro"].index(st.session_state.get("sexo", "Masculino")))

# =======================
# PÁGINA 2 - Saúde e Estilo de Vida
# =======================
with tabs[1]:
    st.title("❤️ Anamnese - Saúde e Estilo de Vida")
    st.markdown("### Forneça informações sobre sua saúde geral.")

    if "saude" not in st.session_state:
        st.session_state.saude = {}

    st.subheader("Histórico Médico")
    condicoes = st.multiselect(
        "Você possui alguma das seguintes condições?",
        ["Hipertensão", "Diabetes", "Problemas Cardíacos", "Problemas Respiratórios (Asma, etc.)", "Dores Articulares Crônicas", "Hérnia de Disco"],
        default=st.session_state.saude.get("condicoes", [])
    )
    st.session_state.saude["condicoes"] = condicoes
    st.session_state.saude["outras_condicoes"] = st.text_area("Outras condições ou cirurgias relevantes?", value=st.session_state.saude.get("outras_condicoes", ""))
    st.session_state.saude["medicamentos"] = st.text_area("Você faz uso de algum medicamento contínuo?", help="Liste os nomes dos medicamentos, se houver.", value=st.session_state.saude.get("medicamentos", ""))

    st.subheader("Estilo de Vida")
    st.session_state.saude["fumante"] = st.radio("Você é fumante?", ["Não", "Sim"], index=["Não", "Sim"].index(st.session_state.saude.get("fumante", "Não")))
    st.session_state.saude["alcool"] = st.select_slider(
        "Com que frequência você consome bebidas alcoólicas?",
        options=["Nunca", "Raramente", "1-2x por semana", "3-4x por semana", "Quase todos os dias"],
        value=st.session_state.saude.get("alcool", "Raramente")
    )
    st.session_state.saude["sono"] = st.slider("Como você avalia a qualidade do seu sono? (1=Péssima, 5=Excelente)", 1, 5, value=st.session_state.saude.get("sono", 3))
    st.session_state.saude["estresse"] = st.slider("Como você avalia seu nível de estresse diário? (1=Baixo, 5=Muito Alto)", 1, 5, value=st.session_state.saude.get("estresse", 3))


# =======================
# PÁGINA 3 - Antropométricos
# =======================
with tabs[2]:
    st.title("📏 Anamnese - Dados Antropométricos")

    if "antropometricos" not in st.session_state:
        st.session_state.antropometricos = {}

    altura_cm = st.number_input("Altura (cm)", min_value=100.0, max_value=250.0, step=0.5, value=st.session_state.antropometricos.get("altura", 170.0), format="%.1f")
    peso = st.number_input("Peso (kg)", min_value=30.0, max_value=250.0, step=0.1, value=st.session_state.antropometricos.get("peso", 70.0), format="%.1f")
    st.session_state.antropometricos["altura"] = altura_cm
    st.session_state.antropometricos["peso"] = peso

    # Cálculo do IMC
    if altura_cm > 0:
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)
        st.metric(label="Seu Índice de Massa Corporal (IMC) é", value=f"{imc:.2f}")
        st.info("Classificação do IMC:\n- Abaixo de 18.5: Abaixo do peso\n- 18.5 - 24.9: Peso normal\n- 25.0 - 29.9: Sobrepeso\n- 30.0 e acima: Obesidade")

    st.subheader("Circunferências (cm)")
    st.session_state.antropometricos["cintura"] = st.number_input("Cintura", min_value=40.0, max_value=200.0, step=0.5, value=st.session_state.antropometricos.get("cintura", 80.0), format="%.1f")
    st.session_state.antropometricos["quadril"] = st.number_input("Quadril", min_value=40.0, max_value=200.0, step=0.5, value=st.session_state.antropometricos.get("quadril", 90.0), format="%.1f")
    st.session_state.antropometricos["torax"] = st.number_input("Tórax", min_value=50.0, max_value=200.0, step=0.5, value=st.session_state.antropometricos.get("torax", 95.0), format="%.1f")
    st.session_state.antropometricos["braco_dir"] = st.number_input("Braço Direito", min_value=20.0, max_value=70.0, step=0.5, value=st.session_state.antropometricos.get("braco_dir", 35.0), format="%.1f")
    st.session_state.antropometricos["braco_esq"] = st.number_input("Braço Esquerdo", min_value=20.0, max_value=70.0, step=0.5, value=st.session_state.antropometricos.get("braco_esq", 35.0), format="%.1f")
    st.session_state.antropometricos["coxa_dir"] = st.number_input("Coxa Direita", min_value=30.0, max_value=90.0, step=0.5, value=st.session_state.antropometricos.get("coxa_dir", 55.0), format="%.1f")
    st.session_state.antropometricos["coxa_esq"] = st.number_input("Coxa Esquerda", min_value=30.0, max_value=90.0, step=0.5, value=st.session_state.antropometricos.get("coxa_esq", 55.0), format="%.1f")
    st.session_state.antropometricos["pant_dir"] = st.number_input("Panturrilha Direita", min_value=20.0, max_value=60.0, step=0.5, value=st.session_state.antropometricos.get("pant_dir", 38.0), format="%.1f")
    st.session_state.antropometricos["pant_esq"] = st.number_input("Panturrilha Esquerda", min_value=20.0, max_value=60.0, step=0.5, value=st.session_state.antropometricos.get("pant_esq", 38.0), format="%.1f")


# =======================
# PÁGINA 4 - Simetria Muscular
# =======================
with tabs[3]:
    st.title("💪 Anamnese - Avaliação Subjetiva de Simetria")
    st.write("Avalie seu nível de desenvolvimento muscular percebido (1 = pouco desenvolvido / 5 = muito desenvolvido)")

    if "simetria" not in st.session_state:
        st.session_state.simetria = {}

    st.session_state.simetria["peitoral"] = st.slider("Peitoral", 1, 5, st.session_state.simetria.get("peitoral", 3))
    st.session_state.simetria["costas"] = st.slider("Costas", 1, 5, st.session_state.simetria.get("costas", 3))
    st.session_state.simetria["ombros"] = st.slider("Ombros", 1, 5, st.session_state.simetria.get("ombros", 3))
    st.session_state.simetria["bracos"] = st.slider("Braços (Bíceps e Tríceps)", 1, 5, st.session_state.simetria.get("bracos", 3))
    st.session_state.simetria["pernas"] = st.slider("Pernas (Quadríceps e Isquiotibiais)", 1, 5, st.session_state.simetria.get("pernas", 3))
    st.session_state.simetria["panturrilhas"] = st.slider("Panturrilhas", 1, 5, st.session_state.simetria.get("panturrilhas", 3))
    st.session_state.simetria["abdomen"] = st.slider("Core/Abdômen", 1, 5, st.session_state.simetria.get("abdomen", 3))


# =======================
# PÁGINA 5 - Objetivos e Experiência
# =======================
with tabs[4]:
    st.title("🎯 Anamnese - Objetivos e Experiência")

    if "objetivos" not in st.session_state:
        st.session_state.objetivos = {}

    st.session_state.objetivos["objetivo"] = st.selectbox("Qual seu objetivo principal?", ["Hipertrofia", "Força", "Resistência", "Recomposição Corporal", "Emagrecimento", "Qualidade de Vida"], index=["Hipertrofia", "Força", "Resistência", "Recomposição Corporal", "Emagrecimento", "Qualidade de Vida"].index(st.session_state.objetivos.get("objetivo", "Hipertrofia")))
    st.session_state.objetivos["nivel"] = st.selectbox("Nível de experiência com treinamento", ["Iniciante (nunca treinou ou treinou por menos de 3 meses)", "Intermediário (treina consistentemente há 6 meses ou mais)", "Avançado (treina consistentemente há vários anos)"], index=["Iniciante (nunca treinou ou treinou por menos de 3 meses)", "Intermediário (treina consistentemente há 6 meses ou mais)", "Avançado (treina consistentemente há vários anos)"].index(st.session_state.objetivos.get("nivel", "Iniciante (nunca treinou ou treinou por menos de 3 meses)")))
    st.session_state.objetivos["dias_treino"] = st.number_input("Dias que pretende treinar por semana", min_value=1, max_value=7, step=1, value=st.session_state.objetivos.get("dias_treino", 3))
    st.session_state.objetivos["historico_lesoes"] = st.text_area("Histórico de lesões ou limitações físicas", value=st.session_state.objetivos.get("historico_lesoes", ""), help="Descreva qualquer lesão, dor crônica ou limitação de movimento que você tenha.")

# =======================
# PÁGINA 6 - Resumo
# =======================
with tabs[5]:
    st.title("✅ Anamnese Completa")
    st.markdown("Confira todos os dados coletados. Se precisar alterar algo, basta voltar à aba correspondente.")

    if st.button("📊 Gerar Resumo"):
        # Extração dos dados para facilitar a leitura
        identificacao = st.session_state.get("nome", "Não preenchido")
        idade = st.session_state.get("idade", "Não preenchido")
        sexo = st.session_state.get("sexo", "Não preenchido")
        saude = st.session_state.get("saude", {})
        antropometria = st.session_state.get("antropometricos", {})
        simetria = st.session_state.get("simetria", {})
        objetivos = st.session_state.get("objetivos", {})

        # Exibição organizada
        st.subheader("🧑 Identificação")
        st.text(f"Nome: {identificacao}")
        st.text(f"Idade: {idade} anos")
        st.text(f"Sexo: {sexo}")

        with st.expander("❤️ Saúde e Estilo de Vida", expanded=True):
            st.write(f"**Condições Médicas:** {', '.join(saude.get('condicoes', [])) if saude.get('condicoes') else 'Nenhuma informada'}")
            st.write(f"**Outras Condições/Cirurgias:** {saude.get('outras_condicoes') or 'Nenhuma'}")
            st.write(f"**Medicamentos em Uso:** {saude.get('medicamentos') or 'Nenhum'}")
            st.write(f"**Fumante:** {saude.get('fumante', 'Não informado')}")
            st.write(f"**Consumo de Álcool:** {saude.get('alcool', 'Não informado')}")
            st.write(f"**Qualidade do Sono (1-5):** {saude.get('sono', 'Não informado')}")
            st.write(f"**Nível de Estresse (1-5):** {saude.get('estresse', 'Não informado')}")

        with st.expander("📏 Dados Antropométricos", expanded=True):
            col1, col2 = st.columns(2)
            col1.metric("Altura", f"{antropometria.get('altura', 0)} cm")
            col2.metric("Peso", f"{antropometria.get('peso', 0)} kg")
            st.text("Circunferências:")
            st.text(f"  - Tórax: {antropometria.get('torax', 0)} cm | Cintura: {antropometria.get('cintura', 0)} cm | Quadril: {antropometria.get('quadril', 0)} cm")
            st.text(f"  - Braços: {antropometria.get('braco_dir', 0)} cm (D) / {antropometria.get('braco_esq', 0)} cm (E)")
            st.text(f"  - Coxas: {antropometria.get('coxa_dir', 0)} cm (D) / {antropometria.get('coxa_esq', 0)} cm (E)")
            st.text(f"  - Panturrilhas: {antropometria.get('pant_dir', 0)} cm (D) / {antropometria.get('pant_esq', 0)} cm (E)")

        with st.expander("💪 Avaliação Subjetiva de Simetria (1-5)", expanded=False):
            st.json(simetria)

        with st.expander("🎯 Objetivos e Experiência", expanded=True):
            st.write(f"**Objetivo Principal:** {objetivos.get('objetivo', 'Não informado')}")
            st.write(f"**Nível de Experiência:** {objetivos.get('nivel', 'Não informado')}")
            st.write(f"**Dias de Treino/Semana:** {objetivos.get('dias_treino', 'Não informado')}")
            st.write(f"**Histórico de Lesões:** {objetivos.get('historico_lesoes') or 'Nenhum'}")

    if st.button("🔄 Limpar e Refazer Anamnese"):
        keys_to_clear = ["nome", "idade", "sexo", "saude", "antropometricos", "simetria", "objetivos"]
        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()